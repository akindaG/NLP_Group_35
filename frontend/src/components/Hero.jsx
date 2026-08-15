import { motion } from "framer-motion";


function Hero(){

    return (

        <section className="relative z-0 overflow-hidden pt-32 min-h-screen bg-slate-950 text-white">


            {/* Background Glow Effects */}

            <div className="absolute top-20 left-20 w-72 h-72 bg-blue-600 rounded-full blur-[140px] opacity-30"></div>

            <div className="absolute bottom-20 right-20 w-96 h-96 bg-purple-600 rounded-full blur-[160px] opacity-20"></div>



            {/* Floating Grid */}

            <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff08_1px,transparent_1px),linear-gradient(to_bottom,#ffffff08_1px,transparent_1px)] bg-[size:60px_60px]"></div>




            <div className="relative z-10 max-w-7xl mx-auto px-6 grid md:grid-cols-2 gap-16 items-center">



                {/* LEFT CONTENT */}


                <motion.div

                    initial={{opacity:0, x:-60}}

                    animate={{opacity:1, x:0}}

                    transition={{duration:0.8}}

                >


                    <h1 className="text-6xl font-bold leading-tight">


                        Transform Customer Support


                        <span className="text-blue-500">

                            {" "}with AI

                        </span>


                    </h1>



                    <p className="mt-6 text-xl text-slate-300 leading-relaxed">


                        Automatically classify tickets,
                        predict priority, analyze sentiment,
                        and route customer issues using
                        advanced NLP models.


                    </p>




                    <div className="mt-8 flex gap-5">


                        <motion.button

                        whileHover={{scale:1.05}}

                        className="bg-blue-600 px-7 py-3 rounded-xl shadow-lg shadow-blue-600/30"

                        >

                            Analyze Ticket

                        </motion.button>



                        <motion.button

                        whileHover={{scale:1.05}}

                        className="border border-slate-600 px-7 py-3 rounded-xl"

                        >

                            View Dashboard

                        </motion.button>



                    </div>


                </motion.div>






                {/* AI CARD */}



                <motion.div


                    initial={{opacity:0, y:60}}

                    animate={{
                        opacity:1,
                         y:[0,-15,0]
                    }}

                    transition={{
                        opacity:{duration:1},
                        y:{
                             duration:4,
                             repeat:Infinity,
                             ease:"easeInOut"
                        }
                    }}


                    className="relative"


                >


                    <div className="absolute inset-0 bg-blue-500 blur-3xl opacity-20"></div>




                    <div className="relative bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl p-8 shadow-2xl">

    {/* Card Header */}
    <div className="flex items-center justify-between mb-8">

        <h3 className="text-2xl font-semibold">
            AI Ticket Analysis
        </h3>

        {/* Live Status Indicator */}
        <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-green-500/10 border border-green-500/20">

            <span className="relative flex h-2.5 w-2.5">

                {/* Pulsing glow */}
                <span className="absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75 animate-ping"></span>

                {/* Actual dot */}
                <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-green-500"></span>

            </span>

            <span className="text-xs font-medium text-green-400">
                AI Online
            </span>

        </div>

    </div>


    <div className="space-y-6">

    {/* Category */}

    <div className="flex justify-between items-center">

        <div>
            <p className="text-slate-400 text-sm">
                Category
            </p>

            <p className="text-xl font-semibold">
                Billing Issue
            </p>
        </div>


        <span className="px-3 py-1 rounded-full bg-blue-500/20 text-blue-400 text-sm">
            NLP
        </span>

    </div>




    {/* Priority */}

    <div className="flex justify-between items-center">


        <div>

            <p className="text-slate-400 text-sm">
                Priority
            </p>

            <p className="text-xl font-semibold text-red-400">
                High
            </p>

        </div>


       <span className="px-3 py-1 rounded-full bg-red-500/20 text-red-400 text-sm">
        High Risk
       </span>


    </div>





    {/* Sentiment */}

    <div className="flex justify-between items-center">


        <div>

            <p className="text-slate-400 text-sm">
                Sentiment
            </p>

            <p className="text-xl font-semibold">
                Negative
            </p>

        </div>


        <span className="px-3 py-1 rounded-full bg-orange-500/20 text-orange-400 text-sm">
               Negative
        </span>


    </div>






    {/* Department */}

    <div>


        <p className="text-slate-400 text-sm">
            Recommended Department
        </p>


        <p className="text-xl font-semibold">
            Finance Support
        </p>


    </div>






    {/* Model Used */}

<div>

    <p className="text-slate-400 text-sm">
        Model Used
    </p>

    <p className="text-xl font-semibold">
        DistilBERT
    </p>

</div>


{/* Confidence */}

<div>

    <div className="flex justify-between mb-2">

        <p className="text-slate-400 text-sm">
            Confidence Score
        </p>

        <p className="text-green-400 font-semibold">
            94.2%
        </p>

    </div>


    <div className="w-full bg-slate-700 rounded-full h-3">

        <div
            className="bg-green-500 h-3 rounded-full"
            style={{width:"94.2%"}}
        >

        </div>

    </div>

</div>






    {/* Keywords */}

    <div>


        <p className="text-slate-400 text-sm mb-3">
            Important Keywords
        </p>


        <div className="flex gap-2 flex-wrap">


            <span className="px-3 py-1 bg-white/10 rounded-full text-sm">
                refund
            </span>


            <span className="px-3 py-1 bg-white/10 rounded-full text-sm">
                payment
            </span>


            <span className="px-3 py-1 bg-white/10 rounded-full text-sm">
                charged
            </span>


        </div>


    </div>



</div>



                    </div>



                </motion.div>




            </div>



        </section>

    )


}


export default Hero;