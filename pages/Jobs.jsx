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