import time

st = time.localtime()
print("%04d-%02d-%02d"%(st.tm_year, st.tm_mon, st.tm_mday))
