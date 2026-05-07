import { useState } from "react";
import { requestJobs } from "../api/client";

export default function Home() {
  const [userId, setUserId] = useState("123");

  const handleSearch = async () => {
    await requestJobs(userId);
    alert("Job search started...");
  };

  return (
    <div>
      <h1>AI Job Agent Dashboard</h1>

      <input
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        placeholder="User ID"
      />

      <button onClick={handleSearch}>
        Search Jobs
      </button>
    </div>
  );
}