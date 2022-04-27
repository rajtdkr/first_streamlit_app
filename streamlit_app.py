
import requests
import streamlit
import pandas


import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
streamlit.header('Fruity Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:   
    streamlit.error('Please select a fruit to get information')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# #streamlit.text(fruityvice_response.json())
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()
#streamlit.stop()


def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute('select * from fruit_load_list')
    return my_cur.fetchall()
if streamlit.button('get Fruit Load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')\

if streamlit.button('Add a Fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("Select Current_user(), Current_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake")



# my_cur.execute("select * from fruit_load_list")
# streamlit.text(my_data_row)
# my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit load list contains")
# streamlit.dataframe(my_data_rows)


# fruit_choice = streamlit.text_input('What fruit would you like to add','Jackfruit')
# streamlit.write('the user entered', fruit_choice)

# my_cur.execute("insert into fruit_load_list values ('from streamlit')");
