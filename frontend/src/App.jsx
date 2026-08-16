import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";


// Pages
import Landing from "./pages/Landing";
import Analyzer from "./pages/Analyzer";
import Dashboard from "./pages/Dashboard";


// Layout
import DashboardLayout from "./layouts/DashboardLayout";



function App() {


  return (


    <BrowserRouter>


      <Routes>



        {/* =========================
            Landing Page
        ========================== */}

        <Route

          path="/"

          element={<Landing />}

        />




        {/* =========================
            AI Ticket Analyzer
        ========================== */}

        <Route

          path="/analyzer"

          element={<Analyzer />}

        />





        {/* =========================
            Enterprise Dashboard
        ========================== */}

        <Route

          path="/dashboard"

          element={

            <DashboardLayout>

              <Dashboard />

            </DashboardLayout>

          }

        />






        {/* =========================
            Default Redirect
        ========================== */}

        <Route

          path="*"

          element={

            <Navigate

              to="/"

              replace

            />

          }

        />



      </Routes>


    </BrowserRouter>


  );

}



export default App;