import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [jobs, setJobs] = useState(null)

  useEffect(() => {
    function fetchJobs() {
      axios.get("http://127.0.0.1:8000/api/job/")
      .then(res => {
        console.log(res.data)
        setJobs(res.data)
      })
    }
    fetchJobs()
  }, [])
  return (
    <div>
      {jobs && jobs.map((job, i) => {
        return (
          <div key={i}>
            Job # {job.id}: {job.title} 
          </div>
        )
      })}
    </div>
  );
}

export default App;
