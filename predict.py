import joblib
import pandas as pd


def get_predict(d: dict):
    model = joblib.load('model.joblib')
    from_sample_df = joblib.load('from_sample.joblib')

    sample = pd.Series(d)
    df_sample = pd.DataFrame(sample, columns=['sample'])
    df_sample = df_sample.T

    df_sample[['year', 'milage', 'engine', 'accident']] = (
        df_sample[['year', 'milage', 'engine', 'accident']].astype('float64'))

    sample_X = df_sample.rename(columns={'brand': df_sample['brand'].values[0],
                                         'color': df_sample['color'].values[0],
                                         'fuel_type': df_sample['fuel_type'].values[0]})

    sample_X[[sample['brand'], sample['color'], sample['fuel_type']]] = 1.0
    df_concat_with_sample = pd.concat([from_sample_df, sample_X]).fillna(0.0)

    sample = df_concat_with_sample.loc['sample']
    sample = pd.DataFrame(sample).T
    prediction = model.predict(sample)
    return prediction[0]


if __name__ == '__main__':
    print(get_predict({'brand': 'brand_Audi', 'year': '2023', 'milage': '0', 'fuel_type': 'fuel_type_Diesel', 'engine': '3.8', 'color': 'color_Gray', 'accident': '1'}))