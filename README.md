<h1><b>Interactive Travel Planner</b></h1>
<h2>Overview</h2>
<p>The Interactive Travel Planner is a web application that helps users plan their travels by providing personalized destination suggestions, itineraries, and activities based on their preferences</p>
<h2>Features</h2>
<ul>
  <li>Users can input their travel preferences, including travel type and activities</li>
  <li>The application uses OpenAI's GPT-3.5 to generate personalized travel suggestions.</li>
  <li>Suggestions include destinations, activities, and itineraries.</li>
  <li>The frontend is built with SvelteKit for a modern and responsive user experience.</li>
  <li>The backend is built with Python FastAPI</li>
</ul>
<h2>Tech Stack</h2>
<ul>
  <li><b>Frontend:</b> SvelteKit</li>
  <li><b>Backend:</b> Python FastAPI</li>
  <li><b>AI Integration:</b> OpenAI GPT-3.5</li>
  <li><b>API Client:</b> RESTful API</li>
</ul>
<h2>Prerequisites</h2>
<ul>
  <li>Node.js and npm (for the frontend)</li>
  <li>Python 3.8+ (for the backend)</li>
  <li>OpenAI API key</li>
</ul>

<h4>Clone the repository:</h4>
<pre><code>
git clone [https://github.com/DevDotJoel/InteractiveTravelPlanner.git]
</code></pre>
<h2>Installation</h2>
<h3>Backend (FastAPI)</h3>
<h4>Set up environment variables:</h4>
<p>Inside the <code>InteractiveTravelPlanner.Api</code> directory, create a <code>.env</code> file and add your OpenAI API key:</p>
<pre><code>OPENAI_API_KEY=your_openai_api_key</code></pre>
<h3>FrontEnd (Sveltekit)</h3>
<p>Inside the <code>InteractiveTravelPlanner.Web</code> directory, run the command <code>npm install</code> and <code>npm run dev</code> to start the project</p>
