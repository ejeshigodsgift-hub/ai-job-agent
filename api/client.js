const BASE_URL = "http://localhost:5000";

export async function getProfile(userId) {
  const res = await fetch(`${BASE_URL}/profile/${userId}`);
  return res.json();
}

export async function getJobs(userId) {
  const res = await fetch(`${BASE_URL}/jobs/search/${userId}`);
  return res.json();
}

export async function generateDocs(userId, jobIndex = 0) {
  const res = await fetch(`${BASE_URL}/generate/${userId}?job=${jobIndex}`);
  return res.json();
}

export async function requestJobs(userId) {
  const res = await fetch(`${BASE_URL}/jobs/request/${userId}`, {
    method: "POST"
  });
  return res.json();
}