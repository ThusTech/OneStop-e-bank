import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Render the App component inside the root element in public/index.html
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
