import numpy as np
import pandas as pd

# 算出 Embarked 最常出現的值
train_df = pd.read_csv('titanic_data/train.csv')
freq_port = train_df.Embarked.dropna().mode()[0]
# Embarked 的缺失值用最常出現的值來補
train_df['Embarked'] = train_df['Embarked'].fillna(freq_port)
train_df[['Embarked', 'Survived']].groupby(['Embarked'], as_index=False).mean().sort_values(by='Survived', ascending=False)

# Age 的缺失值用 Sex 跟 Pclass 群聚後的 Age 平均值來補
train_df['Age'] = train_df['Age'].fillna(train_df.groupby(['Sex', 'Pclass'])['Age'].transform('mean'))
train_df.head(10)

# print(f"丟棄前: {train_df.shape}")
train_df = train_df.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
# print(f"丟棄後: {train_df.shape}")

print(train_df.info())