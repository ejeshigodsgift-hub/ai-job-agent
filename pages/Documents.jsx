import { useState } from "react";
import { generateDocs } from "../api/client";

export default function Documents() {
  const [docs, setDocs] = useState(null);
  const userId = "123";

  const handleGenerate = async () => {
    const res = await generateDocs(userId, 0);
    setDocs(res);
  };

  return (
    <div>
      <h2>Generated Documents</h2>

      <button onClick={handleGenerate}>
        Generate CV Pack
      </button>

      {docs && (
        <div>
          <h3>CV</h3>
          <pre>{docs.cv}</pre>

          <h3>Cover Letter</h3>
          <pre>{docs.cover_letter}</pre>

          <h3>Email</h3>
          <pre>{docs.email}</pre>
        </div>
      )}
    </div>
  );
}