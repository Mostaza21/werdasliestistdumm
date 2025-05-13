import streamlit as st
import random

X = ["Kai", "Aylin", "Chris", "Danny"]
Y = ["Dumpfbacke", "Lootgeier", "Schlaubi-Schlumpf", "Noob", "Klugscheißinator", "Alter Sack", "Synapsenschoner", "RAM-Rentner", "Trottel", "taubes Nüsschen", "Mettigel", "fetter Keks", "XP-Schmarotzer", "Bug in der Matrix", "bisschen zu fett"]

st.title ("Wer das liest ist dumm")

I = None
II = None

if st.button("Klick mich sanft und zärtlich"):

	I = random.choice(X)
	II = random.choice(Y)

st.write(f"**{I}** ist ein **{II}**")
