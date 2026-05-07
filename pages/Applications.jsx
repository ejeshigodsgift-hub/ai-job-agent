import { useEffect, useState } from "react";

const BASE_URL = "http://localhost:5000";

export default function Applications() {
  const [jobs, setJobs] = useState([]);
  const userId = "123";

  useEffect(() => {
    fetch(`${BASE_URL}/jobs/search/${userId}`)
      .then(res => res.json())
      .then(data => setJobs(data.jobs));
  }, []);

  return (
    <div>
      <h1>Job Applications</h1>

      {jobs.map((job, i) => (
        <div key={i}>
          <h3>{job.title}</h3>
          <p>{job.company}</p>

          <button>Generate CV</button>
          <button>Save Job</button>
        </div>
      ))}
    </div>
  );
}