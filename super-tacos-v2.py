import streamlit as st

st.set_page_config(page_title='Super Tacos', page_icon='🌮', layout='wide')

st.markdown('''
<style>
.main {background: linear-gradient(180deg,#fff8f0,#fff);} 
.hero {padding:2rem;border-radius:24px;background:linear-gradient(135deg,#ff914d,#ff4d4d);color:white;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,.15);} 
.card {background:white;padding:1.2rem;border-radius:22px;box-shadow:0 8px 24px rgba(0,0,0,.08);border:1px solid #f2f2f2;height:100%;}
.price {font-size:1.4rem;font-weight:700;color:#ff4d4d;}
.small {color:#666;font-size:.95rem;}
.footer {text-align:center;color:#666;padding:2rem 0;}
</style>
''', unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
<h1>🌮 Super Tacos</h1>
<h3>Fresh • Delicious • Authentic</h3>
<p>Made daily with bold flavors and premium ingredients.</p>
</div>
""", unsafe_allow_html=True)

st.write('')
col1,col2=st.columns(2)
with col1:
    st.info('📞 (555) 123-4567')
with col2:
    st.info('✉️ contact@supertacos.com')

st.markdown('## Our Menu')

items = [
    ('🐔 Chicken Taco','$3.50',['Grilled chicken','Onions','Cilantro','Lettuce','Cheese','Salsa roja']),
    ('🥩 Beef Taco','$4.00',['Seasoned beef','Tomatoes','Onions','Cheese','Lettuce','Sour cream']),
    ('🍍 Pastor Taco','$4.25',['Marinated pork','Pineapple','Onions','Cilantro','Salsa verde'])
]

cols = st.columns(3)
for col, item in zip(cols, items):
    name, price, ingredients = item
    with col:
        st.markdown(f"<div class='card'><h3>{name}</h3><p class='price'>{price}</p><p><b>Ingredients</b></p><ul>" + ''.join([f'<li>{i}</li>' for i in ingredients]) + "</ul><p class='small'>Served on warm corn tortillas.</p></div>", unsafe_allow_html=True)

st.write('')
st.button('🛒 Order Now')

st.markdown("<div class='footer'>Thank you for visiting Super Tacos 🌮</div>", unsafe_allow_html=True)
