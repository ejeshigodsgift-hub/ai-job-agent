export default function LandingPage() {
  return (
    <div style={{ padding: 40 }}>

      <h1>AI Job Agent</h1>

      <p>
        Your personal AI that finds jobs, builds CVs, and applies for you automatically.
      </p>

      <button>Get Started Free</button>

      <Features />
      <Pricing />
    </div>
  );
}


variant = get_variant(user_id)

if variant == "A":
    headline = "Find Jobs Faster with AI"
else:
    headline = "Your AI Career Agent Works for You"