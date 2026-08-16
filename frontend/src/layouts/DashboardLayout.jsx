import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";


function DashboardLayout({ children }) {


    return (

        <div className="
            min-h-screen
            bg-slate-950
            text-white
            flex
        ">


            <Sidebar />


            <div className="
                flex-1
                flex
                flex-col
            ">


                <Topbar />


                <main className="
                    flex-1
                    overflow-y-auto
                ">

                    {children}

                </main>


            </div>


        </div>

    )

}


export default DashboardLayout;