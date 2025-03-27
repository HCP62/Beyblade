from flask import Flask, render_template, request, jsonify
from beyblade import Beyblade
from match import Match

app = Flask(__name__)

# Store active matches in memory (in production, you'd want to use a database)
active_sets = {}

class MatchSet:
    def __init__(self, bey1, bey2):
        self.bey1 = bey1
        self.bey2 = bey2
        self.matches_played = 0
        self.bey1_match_wins = 0
        self.total_battles = 0
        self.bey1_battle_wins = 0
        self.victory_types = {
            'spin': 0,
            'over': 0,
            'burst': 0,
            'x': 0
        }
        self.current_match = Match(bey1, bey2)

    def get_stats(self):
        # Calculate win percentages
        match_win_rate = (self.bey1_match_wins / max(self.matches_played, 1) * 100)
        battle_win_rate = (self.bey1_battle_wins / max(self.total_battles, 1) * 100)
        
        # Calculate victory type percentages (out of bey1's wins only)
        victory_percentages = {}
        if self.bey1_battle_wins > 0:
            for vt, count in self.victory_types.items():
                percentage = (count / self.bey1_battle_wins * 100)
                victory_percentages[vt] = round(percentage, 2)
        else:
            victory_percentages = {vt: 0 for vt in self.victory_types}
        
        return {
            'matches_played': self.matches_played,
            'match_wins': self.bey1_match_wins,
            'total_battles': self.total_battles,
            'match_win_rate': round(match_win_rate, 2),
            'battle_win_rate': round(battle_win_rate, 2),
            'victory_types': self.victory_types,
            'victory_percentages': victory_percentages
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_matchset', methods=['POST'])
def create_matchset():
    try:
        data = request.json
        print("Received data:", data)  # Debug print
        
        bey1 = Beyblade(
            data['bey1']['blade'],
            data['bey1']['ratchet'],
            data['bey1']['bit']
        )
        bey2 = Beyblade(
            data['bey2']['blade'],
            data['bey2']['ratchet'],
            data['bey2']['bit']
        )
        
        match_set = MatchSet(bey1, bey2)
        set_id = len(active_sets)
        active_sets[set_id] = match_set
        
        return jsonify({
            'set_id': set_id,
            'bey1': str(bey1),
            'bey2': str(bey2)
        })
    except Exception as e:
        print("Error:", str(e))  # Debug print
        return jsonify({'error': str(e)}), 500

@app.route('/record_battle', methods=['POST'])
def record_battle():
    data = request.json
    match_set = active_sets[data['set_id']]
    current_match = match_set.current_match
    
    winner_bey = current_match.get_bey1() if data['winner'] == 1 else current_match.get_bey2()
    current_match.battle_gui(winner_bey, data['victory_type'])
    
    # Update total battles and bey1 wins
    match_set.total_battles += 1
    if data['winner'] == 1:
        match_set.bey1_battle_wins += 1
        match_set.victory_types[data['victory_type']] += 1
    
    # Check if current match is over
    match_over = current_match.get_bey1_points() >= 4 or current_match.get_bey2_points() >= 4
    
    # If match is over, update match stats before creating response
    if match_over:
        match_set.matches_played += 1
        if current_match._winner == match_set.bey1:
            match_set.bey1_match_wins += 1
    
    response_data = {
        'battles': current_match.get_battles(),
        'bey1_points': current_match.get_bey1_points(),
        'bey2_points': current_match.get_bey2_points(),
        'winner': str(current_match._winner) if current_match._winner else None,
        'matches_completed': match_set.matches_played,
        'stats': match_set.get_stats(),
        'match_over': match_over
    }
    
    # If match is over, prepare for next match
    if match_over and match_set.matches_played < 10:
        match_set.current_match = Match(match_set.bey1, match_set.bey2)
        response_data['new_match'] = True
    elif match_set.matches_played >= 10:
        response_data['set_complete'] = True
            
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True) 