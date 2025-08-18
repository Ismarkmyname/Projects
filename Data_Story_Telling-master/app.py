import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as mpl
from matplotlib import style
import matplotlib.pyplot as plt

df = pd.read_csv('USA_cars_datasets.csv')

st.title("Data Storytelling ")
st.write("1. How does price vary across different car brands?")

car_brands = df["brand"].unique()
average_sale_prices = df.groupby("brand")["price"].mean()
model_years = df.groupby("brand")["year"].first()
fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(range(len(car_brands)), average_sale_prices, c=model_years, cmap='viridis')
ax.set_xlabel("Car Brand")
ax.set_ylabel("Average Sale Price ($)")
ax.set_title("Average Sale Price by Car Brand (Color-Coded by Model Year)")
ax.set_xticks(ticks=range(len(car_brands)), labels=car_brands, rotation=50, ha="right")
fig.colorbar(ax.get_children()[0], label="Model Year")
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)

st.write("Insight: Makikita dito kung ano ano ang mga brand na may pinaka mahal at may pinaka murang kotse.")
st.write("2. How does price change with vehicle age?")

df['age'] = 2024 - df['year']
avg_price_age = df.groupby('age')['price'].mean()
avg_price_mileage = df.groupby('mileage')['price'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(avg_price_age.index, avg_price_age, label='Average Price by Age')
ax.plot(avg_price_mileage.index, avg_price_mileage, label='Average Price by Mileage')
ax.set_xlabel('Vehicle Age (Years) / Mileage')
ax.set_ylabel('Average Sale Price ($)')
ax.set_title('Depreciation Trends: Average Price by Age and Mileage')
ax.legend()
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)

st.write("Insight: Makikita sa graph kung paano yung pag baba ng price ng kotse base sa kung gaano na ito ka luma")
st.write("3. Does the location of the car impact its price?")

average_price_by_location = df.groupby('country')['price'].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='country', y='price', data=average_price_by_location, ax=ax)
st.pyplot(fig)

st.write("Insight: Makikita sa graph na malaki ang pinag kaiba ng price ng kotse depende sa country")
st.write("4. How does the condition of the car title affect its price?")

def create_bar_chart(segment_by='year'):
 
    fig, ax = plt.subplots(figsize=(10, 6))

    average_price = df.groupby([segment_by, 'title_status'])['price'].mean().unstack()
    average_price.plot(kind='bar', width=0.8, color=['skyblue', 'lightcoral'], ax=ax)

    ax.set_xlabel(segment_by)
    ax.set_ylabel('Average Price ($)')
    ax.set_title(f"Average Car Price by Year and Title Status")
    ax.legend(title='Title Status')
    ax.tick_params(rotation=45)
    ax.grid(axis='y')
    plt.tight_layout()

    return fig

fig = create_bar_chart()
st.pyplot(fig)

st.write("Insight: Makikita dito ang pinagkaiba sa presyo ng clean at salvage car title ang ibig sabihin lang ng kotse na may salvage title ay masira ang kotse dahil sa aksidente(na bangga most of the time) at inayos lang ulit")
st.write("5. How does the price of a car vary across different car lots?")

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['lot'], df['price'], c=df['year'], cmap='viridis', alpha=0.7)
ax.set_xlabel('Car Lot')
ax.set_ylabel('Price ($)')
ax.set_title('Car Price by Lot (Colored by Model Year)')
ax.grid(True)
fig.colorbar(ax.get_children()[0], label='Model Year')
plt.tight_layout()
st.pyplot(fig)

st.write("Insight: base sa https://www.kaggle.com/datasets/doaaalsenani/usa-cers-dataset A lot number is an identification number assigned to a particular quantity or lot of material from a single manufacturer.For cars, a lot number is combined with a serial number to form the Vehicle Identification Number. So makikita sa graph ang pinag kaiba at pinag ka pareho ng presyo ng mga kotse na ginawa sa specific na lot.")