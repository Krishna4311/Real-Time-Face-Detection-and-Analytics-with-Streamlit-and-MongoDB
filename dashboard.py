from libs import *
from db import collection

# --- Page Config ---
st.set_page_config(page_title="Face Detection Dashboard", layout="wide")
st.title("Face Detection Dashboard")
st.markdown("Generated from raw MongoDB logs (real-time face counts).")

# --- Sidebar Options ---
st.sidebar.title("Controls")
auto_refresh = st.sidebar.checkbox("Auto-refresh every 10s", value=False)
manual_refresh = st.sidebar.button("Refresh Now")

if auto_refresh:
    st_autorefresh(interval=10000, key="auto-refresh")

# --- Load Logs ---
@st.cache_data(ttl=10)
def load_logs():
    return list(collection.find({}))

if manual_refresh:
    st.cache_data.clear()

raw_logs = load_logs()
if not raw_logs:
    st.warning("No detection logs found.")
    st.stop()

# --- DataFrame ---
df = pd.DataFrame(raw_logs)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["minute"] = df["timestamp"].dt.floor("T")
df["hour"] = df["timestamp"].dt.hour
df["date"] = df["timestamp"].dt.date

# --- Graph: Face Count per Minute ---
st.subheader("Detected Face Count per Minute")
minute_df = df.groupby("minute")["face_count"].sum()
fig1, ax1 = plt.subplots(figsize=(10, 4))
minute_df.plot(ax=ax1)
ax1.set_title("Face Count per Minute")
ax1.set_xlabel("Time")
ax1.set_ylabel("Face Count")
plt.xticks(rotation=45)
st.pyplot(fig1)

# --- Graph: Avg Face Count by Hour ---
st.subheader("Average Face Count by Hour")
hourly_df = df.groupby("hour")["face_count"].mean()
fig2, ax2 = plt.subplots(figsize=(8, 8))
hourly_df.plot(kind="bar", color="orange", ax=ax2)
ax2.set_title("Avg Face Count by Hour")
ax2.set_xlabel("Hour of Day")
ax2.set_ylabel("Average Faces")
st.pyplot(fig2)

# --- Graph: Heatmap Date vs Hour ---
st.subheader("Heatmap: Face Count by Hour & Date")
pivot = df.pivot_table(values='face_count', index='date', columns='hour', aggfunc='sum', fill_value=0)
fig3, ax3 = plt.subplots(figsize=(12, 6))
im = ax3.imshow(pivot, cmap='YlOrRd', aspect='auto')
ax3.set_xticks(np.arange(len(pivot.columns)))
ax3.set_xticklabels(pivot.columns)
ax3.set_yticks(np.arange(len(pivot.index)))
ax3.set_yticklabels(pivot.index)
plt.setp(ax3.get_xticklabels(), rotation=45, ha="right")
fig3.colorbar(im, ax=ax3, label='Face Count')
ax3.set_title("Heatmap of Face Counts")
ax3.set_xlabel("Hour of Day")
ax3.set_ylabel("Date")
st.pyplot(fig3)

# --- Raw Log Table + CSV ---
st.subheader("Raw Detection Logs")
st.dataframe(df[["timestamp", "face_count"]].sort_values("timestamp", ascending=False))

csv = df[["timestamp", "face_count"]].to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "face_logs.csv", "text/csv")
