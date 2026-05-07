import { useEffect, useState } from "react";
import { getJobs } from "../api/client";

export default function Jobs() {
  const [jobs, setJobs] = useState([]);
  const userId = "123";

  useEffect(() => {
    getJobs(userId).then((res) => setJobs(res.jobs));
  }, []);

  return (
    <div>
      <h2>Top Jobs</h2>

      {jobs?.map((job, i) => (
        <div key={i}>
          <h3>{job.title}</h3>
          <p>{job.company}</p>
          <p>{job.location}</p>
        </div>
      ))}
    </div>
  );
}


import { useEffect, useState } from "react";
import { socket } from "../api/socket";

export default function Jobs() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    socket.on("job_update", (data) => {
      setJobs((prev) => [...prev, data.job]);
    });
  }, []);

  return (
    <div>
      <h1>Live Jobs</h1>

      {jobs.map((job, i) => (
        <div key={i}>
          <h3>{job.title}</h3>
          <p>{job.company}</p>
        </div>
      ))}
    </div>
  );
}