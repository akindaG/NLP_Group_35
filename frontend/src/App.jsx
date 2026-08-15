import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import Analyzer from "./pages/Analyzer";
import Dashboard from "./pages/Dashboard";


function App() {

  return (

    <BrowserRouter>

      <Routes>


        {/* Landing Page */}
        <Route
          path="/"
          element={<Landing />}
        />


        {/* AI Ticket Analyzer */}
        <Route
          path="/analyzer"
          element={<Analyzer />}
        />


        {/* Analytics Dashboard */}
        <Route
          path="/dashboard"
          element={<Dashboard />}
        />


      </Routes>

    </BrowserRouter>

  )

}


export default App;