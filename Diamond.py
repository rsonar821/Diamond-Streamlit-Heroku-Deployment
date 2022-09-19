import streamlit as st
from PIL import Image

st.header('About Diamonds')

about = '''Diamond is a solid form of the element carbon with its atoms arranged in a crystal structure called 
diamond cubic. At room temperature and pressure, another solid form of carbon known as graphite is the 
chemically stable form of carbon, but diamond converts to it extremely slowly. Diamond has the highest 
hardness and thermal conductivity of any natural material, properties that are used in major industrial 
applications such as cutting and polishing tools. They are also the reason that diamond anvil cells can 
subject materials to pressures found deep in the Earth. Because the arrangement of atoms in diamond is 
extremely rigid, few types of impurity can contaminate it (two exceptions are boron and nitrogen). 
Small numbers of defects or impurities (about one per million of lattice atoms) color diamond blue (boron), 
yellow (nitrogen), brown (defects), green (radiation exposure), purple, pink, orange, or red. 
Diamond also has a very high refractive index and a relatively high optical dispersion.'''
st.markdown(about)

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    image = Image.open('images/diamond.jpg')
    st.image(image, caption='Diamonds')

with col3:
    st.write("")

st.header('Diamond Features')
st.subheader('Diamond Cut')
st.markdown("""A diamond cut is a style or design guide used when shaping a diamond for polishing such as the 
brilliant cut. Cut does not refer to shape (pear, oval), but the symmetry, proportioning and polish of a 
diamond. The cut of a diamond greatly affects a diamond's brilliance; this means if it is cut poorly, it will 
be less luminous.In order to best use a diamond gemstone's material properties, a number of different diamond 
cuts have been developed. A diamond cut constitutes a more or less symmetrical arrangement of facets, which 
together modify the shape and appearance of a diamond crystal. Diamond cutters must consider several factors, 
such as the shape and size of the crystal, when choosing a cut. The practical history of diamond cuts can be 
traced back to the Middle Ages, while their theoretical basis was not developed until the turn of the 20th 
century. Design, creation and innovation continue to the present day: new technology—notably laser cutting 
and computer-aided design—has enabled the development of cuts whose complexity, optical performance, and 
waste reduction were hitherto unthinkable.""")

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    image = Image.open('images/cut.jpg')
    st.image(image, caption='Diamond Cut')

with col3:
    st.write("")

st.subheader('Diamond Clarity')
st.markdown("""Diamond clarity is the quality of diamonds that relates to the existence and visual appearance 
of internal characteristics of a diamond called inclusions, and surface defects, called blemishes. Clarity is 
one of the four Cs of diamond grading, the others being carat, color, and cut. Inclusions are solids, 
liquids, or gases that were trapped in a mineral as it formed. They may be crystals of a foreign material 
or even another diamond crystal, or may have produced structural imperfections, such as tiny cracks that 
make a diamond appear whitish or cloudy. The number, size, color, relative location, orientation, and 
visibility of inclusions can all affect the relative clarity of a diamond. A clarity grade is assigned 
based on the overall appearance of the stone under ten times magnification, which is the standard 
magnification for loupes used in the gem world.""")

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    image = Image.open('images/clarity.jpg')
    st.image(image, caption='Diamond Clarity')

with col3:
    st.write("")

st.subheader('Diamond Color')
st.markdown("""A chemically pure and structurally perfect diamond is perfectly transparent with no hue, 
or color. However, in reality almost no gem-sized natural diamonds are absolutely perfect. The color of a 
diamond may be affected by chemical impurities and/or structural defects in the crystal lattice. Depending 
on the hue and intensity of a diamond's coloration, a diamond's color can either detract from or enhance 
its value. For example, most white diamonds are discounted in price when more yellow hue is detectable, 
while intense pink diamonds or blue diamonds (such as the Hope Diamond) can be dramatically more valuable. 
Of all colored diamonds, red diamonds are the rarest. The Aurora Pyramid of Hope displays a spectacular 
array of naturally colored diamonds, including red diamonds.""")

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    image = Image.open('images/color.jpg')
    st.image(image, caption='Diamond Color')

with col3:
    st.write("")

st.subheader('Diamond Carat')
st.markdown("""A 'carat' is a unit of measurement used in the diamond industry to specify the weight of a 
diamond. A carat is equal to 200 milligrams, so a 5-carat stone weighs 1 gram. People often mistakenly 
assume that a diamond's size is synonymous with its carat weight, which is not always the case. Like a 
human body, the bigger the diamond is, the heavier it is likely to be, but other factors can also affect 
the size. The manner in which a diamond is cut, for example, has a significant impact on its diameter and 
brilliance. Diamonds with a poorer cut, such as a change of depth or a thick girdle, will retain their heavy 
weight but will be 'hidden' in the base of the diamond with less surface on top, making it appear smaller.""")

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    image = Image.open('images/carat.jpg')
    st.image(image, caption='Diamond Carat')

with col3:
    st.write("")