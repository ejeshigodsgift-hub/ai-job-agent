import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/profile">Profile</Link>
      <Link to="/jobs">Jobs</Link>
      <Link to="/documents">Documents</Link>
    </nav>
  );
}