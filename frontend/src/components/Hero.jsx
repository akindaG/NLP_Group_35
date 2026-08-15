function Hero(){

    return (

        <section className="pt-32 min-h-screen bg-slate-950 text-white">

            <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-2 gap-12 items-center">


                {/* Left Side */}

                <div>


                    <h1 className="text-6xl font-bold leading-tight">

                        Transform Customer Support
                        <span className="text-blue-500">
                            {" "}with AI
                        </span>

                    </h1>


                    <p className="mt-6 text-xl text-slate-300">

                        Automatically classify tickets,
                        predict priority, analyze sentiment,
                        and route customer issues using
                        advanced NLP models.

                    </p>



                    <div className="mt-8 flex gap-5">


                        <button className="bg-blue-600 px-6 py-3 rounded-xl hover:bg-blue-700">

                            Analyze Ticket

                        </button>


                        <button className="border border-slate-600 px-6 py-3 rounded-xl hover:bg-slate-800">

                            View Dashboard

                        </button>


                    </div>


                </div>



                {/* Right Prediction Card */}


                <div className="bg-slate-900 border border-slate-700 rounded-2xl p-8 shadow-xl">


                    <h3 className="text-xl font-semibold mb-6">

                        AI Ticket Analysis

                    </h3>



                    <div className="space-y-5">


                        <div>
                            <p className="text-slate-400">
                                Category
                            </p>

                            <p className="text-lg">
                                Billing Issue
                            </p>
                        </div>



                        <div>
                            <p className="text-slate-400">
                                Priority
                            </p>

                            <p className="text-lg text-red-400">
                                High
                            </p>
                        </div>



                        <div>
                            <p className="text-slate-400">
                                Sentiment
                            </p>

                            <p className="text-lg">
                                Negative
                            </p>
                        </div>



                        <div>
                            <p className="text-slate-400">
                                Confidence
                            </p>

                            <p className="text-lg text-green-400">
                                94.2%
                            </p>
                        </div>


                    </div>


                </div>


            </div>


        </section>

    )

}


export default Hero;