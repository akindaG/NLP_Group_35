import { Link } from "react-router-dom";


function Navbar(){

    return (

        <nav className="fixed top-0 left-0 w-full z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800">

            <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">


                {/* Logo */}

                <Link
                to="/"
                className="text-2xl font-bold text-white"
                >

                    SupportIQ AI

                </Link>



                {/* Navigation */}

                <div className="flex gap-8 text-slate-300">


                    <Link
                    to="/"
                    className="hover:text-white"
                    >
                        Home
                    </Link>


                    <Link
                    to="/dashboard"
                    className="hover:text-white"
                    >
                        Dashboard
                    </Link>


                    <Link
                    to="/analyzer"
                    className="hover:text-white"
                    >
                        Analyzer
                    </Link>


                    <Link
                    to="/models"
                    className="hover:text-white"
                    >
                        Models
                    </Link>


                </div>



                <button className="bg-blue-600 px-5 py-2 rounded-lg text-white hover:bg-blue-700">

                    Get Started

                </button>


            </div>


        </nav>

    )

}


export default Navbar;