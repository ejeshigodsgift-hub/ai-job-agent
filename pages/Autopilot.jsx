import { useEffect, useState } from "react";

const BASE_URL = "http://localhost:5000";

export default function Autopilot() {
  const [data, setData] = useState([]);
  const userId = "123";

  useEffect(() => {
    fetch(`${BASE_URL}/autopilot/results/${userId}`)
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div>
      <h1>AI Autopilot Dashboard</h1>

      {data.map((item, index) => (
        <div key={index} style={{ border: "1px solid #ccc", margin: 10 }}>
          <h3>{item.job.title}</h3>
          <p>{item.job.company}</p>

          <h4>CV</h4>
          <pre>{item.cv}</pre>

          <h4>Cover Letter</h4>
          <pre>{item.cover_letter}</pre>

          <h4>Email</h4>
          <pre>{item.email}</pre>

          <button>Approve Application</button>
          <button>Reject</button>
        </div>
      ))}
    </div>
  );
}


import { useEffect, useState } from "react";
import { socket } from "../api/socket";

export default function Autopilot() {
  const [updates, setUpdates] = useState([]);

  useEffect(() => {
    const userId = "123";

    socket.emit("join", { user_id: userId });

    socket.on("autopilot_update", (data) => {
      setUpdates((prev) => [...prev, data.data]);
    });

    return () => socket.disconnect();
  }, []);

  return (
    <div>
      <h1>Live Autopilot Feed</h1>

      {updates.map((u, i) => (
        <div key={i}>
          <p>{u.status}</p>
        </div>
      ))}
    </div>
  );
}