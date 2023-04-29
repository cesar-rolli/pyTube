import React, {useEffect, useState} from 'react';
import axios from "axios";
import './App.css';

function App() {
  const [initialData, setInitialData] = useState([{}]);
  
  // receive
  useEffect(() => {
    fetch('/api')
    .then(response => response.json())
    .then(data => setInitialData(data))
  }, []);
  
  // send
  const [data, setData] = useState({link: '', resolution: ''});
  const handleChange = (event) => {
    setData(values => ({...values, [event.target.name]: event.target.value}))
  }
  
  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('/youtube', data)
    .then(() => {
      console.log(data.link, data.resolution);
    });
  };

  return (
    <div className="App">
      <form className="column"
        onSubmit={handleSubmit}>
        <div className="row">
          <p>YouTube link:</p>
          <input 
            type="text" 
            name="link" 
            className="input_link"
            value={data.link}
            onChange={handleChange}
            />
        </div>
        <div className="row">
          <p>Resolution (720p, 1080p, 2160p, 4320p):</p>
          <input 
            type="text" 
            name="resolution"
            className="input_res"
            value={data.resolution}
            onChange={handleChange}
            />
        </div>
        <button name="submit" className="button">Download</button>
      </form>
      <div className="list">
      </div>
    </div>
  );
}

export default App;
