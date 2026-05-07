import { useEffect, useState } from "react";

const BASE_URL = "http://localhost:5000";

export default function ActivityLog() {
  const [logs, setLogs] = useState([]);
  const userId = "123";

  useEffect(() => {
    fetch(`${BASE_URL}/activity/${userId}`)
      .then(res => res.json())
      .then(setLogs);
  }, []);

  return (
    <div>
      <h1>AI Activity Log</h1>

      {logs.map((log, i) => (
        <div key={i}>
          <p>{log.action}</p>
          <small>{log.time}</small>
        </div>
      ))}
    </div>
  );
}