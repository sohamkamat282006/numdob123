
import streamlit as st

def sum_digits(n):
    return sum(int(d) for d in str(n))

def digital_root(n):
    while n >= 10:
        n = sum_digits(n)
    return n

st.set_page_config(page_title="Numerology DOB Grid", layout="centered")

st.title("🔢 Numerology DOB Grid")
dob = st.text_input("Enter DOB (DD/MM/YYYY)", max_chars=10)

grid_layout = {
    4: (0, 0), 9: (0, 1), 2: (0, 2),
    3: (1, 0), 5: (1, 1), 7: (1, 2),
    8: (2, 0), 1: (2, 1), 6: (2, 2)
}

grid_data = {k: [] for k in range(1, 10)}

if dob and len(dob) == 10 and dob[2] == '/' and dob[5] == '/':
    digits = [int(ch) for ch in dob if ch.isdigit()]
    total_sum = sum(digits)

    for d in digits:
        if d != 0:
            grid_data[d].append(str(d))

    # Day root
    day_digits = dob[:2]
    day_sum = int(day_digits[0]) + int(day_digits[1])
    day_root = digital_root(day_sum)
    grid_data[day_root].append(str(day_root))

    # Total root
    total_root = digital_root(total_sum)
    grid_data[total_root].append(str(total_root))

    st.subheader("📋 Digit Grid")
    grid_cells = [["" for _ in range(3)] for _ in range(3)]
    for digit, (r, c) in grid_layout.items():
        grid_cells[r][c] = " ".join(grid_data[digit])

    st.table(grid_cells)

    st.markdown(f"### 🔵 Day sum: `{day_root}`")
    st.markdown(f"### 🟠 Total sum: `{total_root}`")
else:
    if dob:
        st.warning("Please enter a valid DOB in DD/MM/YYYY format.")
