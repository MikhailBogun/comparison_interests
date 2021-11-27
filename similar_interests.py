import pandas as pd
import numpy as np
from scipy.spatial import distance

global_dataframe = pd.read_csv("train_interests.csv",header = 0)
columns_title = list(global_dataframe.columns)
basic_dist = dict(zip(columns_title, [0 for i in range(len(columns_title))]))


def change_dataframe(dataframe):
    new_df = dataframe.copy()
    new_df[np.isnan(new_df)] = 0
    new_df[np.isnan(new_df)] = 0
    for i in columns_title:
        new_df.loc[new_df[i] < 3, i] = 0
        new_df.loc[new_df[i] >= 3, i] = 1
    interest_array = new_df.to_numpy()
    return interest_array


def similar_interests(interests, dataframe=None):
    try:
        if dataframe is None:
            interest_array = change_dataframe(global_dataframe)
        else:
            df = pd.DataFrame(dataframe)
            interest_array = change_dataframe(df)
        for key in interests:
            if key in basic_dist:
                basic_dist[key] = 1
        interests = list(basic_dist.values())
        distances = dict()
        for i in range(interest_array.shape[0]):
            distances[i] = distance.cosine(interests, interest_array[i])
        distances_sorted = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
        count = 0
        final_associate_arr = np.array(interests)
        for key in distances_sorted:
            count += 1
            if (count > len(distances_sorted) / 4):
                break
            final_associate_arr = final_associate_arr + interest_array[key]
        best_interests = dict(zip(columns_title, final_associate_arr))
        best_interests_sorted = {k: v for k, v in
                                 sorted(best_interests.items(), key=lambda item: item[1], reverse=True)}.keys()
        return list(best_interests_sorted)
    except:
        return []

if __name__ == '__main__':
    outp = similar_interests(['Books', 'Music', 'Children', 'Outdoors', 'Science_and_technology', 'Foreign languages', 'Cinematography', 'Communication', 'Eating', 'Cybersport', 'Volunteer', 'Pets', 'Sport', 'Dance', 'Concerts', 'Cars', 'Art'])
    print(outp)