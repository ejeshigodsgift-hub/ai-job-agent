import { useEffect, useState } from "react";
import { getProfile } from "../api/client";

export default function Profile() {
  const [profile, setProfile] = useState({});
  const userId = "123";

  useEffect(() => {
    getProfile(userId).then(setProfile);
  }, []);

  return (
    <div>
      <h2>Profile</h2>

      <p>Name: {profile.name}</p>
      <p>Email: {profile.email}</p>
      <p>Phone: {profile.phone}</p>
      <p>Skills: {profile.skills?.join(", ")}</p>
    </div>
  );
}