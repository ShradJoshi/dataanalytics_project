#import dependencies
import json
import statistics

def get_games():
    '''Import JSON data from the game'''
    with open("./data.json") as f:
        data = json.loads(f.read())
        games = data["games"]
        return games

def calculate_success_rate():
    '''Function to calculate success percentage'''
    games = get_games()
    results = []
    for game in games:
        correct_per = game['correct']
        wrong_per = game['wrong']
        total_num_ofnotes_respondedto = correct_per + wrong_per
        total_per = correct_per / total_num_ofnotes_respondedto * 100
        print(total_per)
        results.append(total_per)

    return results

def calculate_response_time():
    '''Function to calculate response time'''
    games = get_games()
    results = []
    labels = []
    for game in games:
        gameresults = []
        started_at = game['startedAt']
        for i, answer in enumerate(game['answers']):
            time_answered = answer['timeAnswered']
            if i == 0:
                response_time = (time_answered - started_at) / 1000
                gameresults.append(response_time)
            else:
                previous_answered = (time_answered - game['answers'][i-1]['timeAnswered']) / 1000
                gameresults.append(previous_answered)
        avg_results = statistics.mean(gameresults)
        results.append(avg_results)
        labels.append(started_at)
    print(results,labels)


#calculate_success_rate()
calculate_response_time()

