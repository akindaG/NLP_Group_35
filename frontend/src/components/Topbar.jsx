import {
    Search,
    Bell,
    Zap,
    Ticket,
    ChevronDown,
    Command
} from "lucide-react";

import { motion } from "framer-motion";
import { useEffect, useState } from "react";

import { getHealth } from "../services/api";



function Topbar(){


const [health,setHealth] = useState({
    status:"checking",
    models:"loading",
    latency:null
});



useEffect(()=>{


const checkHealth = async()=>{

    try{

        const start = Date.now();

        const data = await getHealth();

        const latency = Date.now() - start;


        setHealth({
            ...data,
            latency
        });


    }catch(error){


        setHealth({

            status:"offline",
            models:"unavailable",
            latency:null

        });


    }


};


checkHealth();


const interval = setInterval(
    checkHealth,
    30000
);


return ()=>clearInterval(interval);


},[]);



return(

<motion.header

initial={{
opacity:0,
y:-15
}}

animate={{
opacity:1,
y:0
}}

transition={{
duration:0.5
}}

className="
h-16
sticky
top-0
z-50
bg-slate-950/80
backdrop-blur-xl
border-b
border-white/10
flex
items-center
justify-between
px-8
"

>


{/* BRAND */}

<div>

<h2 className="
text-white
font-semibold
text-lg
">

AI Support Platform

</h2>


<p className="
text-xs
text-slate-500
">

Enterprise NLP Intelligence System

</p>


</div>





{/* SEARCH */}

<div className="
hidden
lg:flex
items-center
gap-3
w-[420px]
h-10
px-4
rounded-xl
bg-white/5
border
border-white/10
">


<Search
size={18}
className="text-slate-400"
/>


<input

placeholder="
Search tickets, models, reports...
"

className="
flex-1
bg-transparent
outline-none
text-sm
text-white
placeholder:text-slate-500
"

/>



<div className="
flex
items-center
gap-1
px-2
py-1
rounded-md
bg-white/10
text-xs
text-slate-400
">

<Command size={12}/>

K

</div>


</div>







<div className="
flex
items-center
gap-3
">



{/* TICKETS */}

<div className="
hidden
xl:flex
items-center
gap-3
px-4
py-2
rounded-xl
bg-blue-500/10
border
border-blue-400/20
">


<Ticket
size={18}
className="text-blue-400"
/>


<div>

<p className="
text-xs
font-semibold
text-blue-400
">

Live

</p>


<p className="
text-[10px]
text-slate-400
">

Current Session

</p>


</div>


</div>







{/* API STATUS */}

<div className="
hidden
md:flex
items-center
gap-3
px-4
py-2
rounded-xl
bg-green-500/10
border
border-green-400/20
">


<div className="
relative
">

<span className="
absolute
w-3
h-3
rounded-full
bg-green-400
animate-ping
"/>


<span className="
relative
block
w-3
h-3
rounded-full
bg-green-400
"/>


</div>



<div>

<p className={`
text-xs
font-semibold
${health.status==="healthy"
?"text-green-400"
:"text-red-400"}
`}>

{
health.status==="healthy"
?
"API Healthy"
:
"API Offline"
}

</p>


<p className="
text-[10px]
text-slate-400
">

{
health.models==="loaded"
?
"Models Ready"
:
"Loading..."
}

</p>


</div>


</div>







{/* LATENCY */}

<div className="
hidden
lg:flex
items-center
gap-2
px-4
py-2
rounded-xl
bg-purple-500/10
border
border-purple-400/20
">


<Zap
size={17}
className="text-purple-400"
/>



<div>

<p className="
text-xs
font-semibold
text-purple-400
">

{
health.latency
?
`${health.latency}ms`
:
"--"
}

</p>


<p className="
text-[10px]
text-slate-400
">

AI Latency

</p>


</div>


</div>







{/* NOTIFICATION */}

<button className="
relative
w-10
h-10
rounded-xl
bg-white/5
border
border-white/10
flex
items-center
justify-center
">

<Bell
size={19}
className="text-slate-300"
/>


<span className="
absolute
top-2
right-2
w-2
h-2
rounded-full
bg-blue-400
"/>


</button>







{/* USER */}

<div className="
flex
items-center
gap-3
px-3
py-2
rounded-xl
hover:bg-white/5
cursor-pointer
">


<div className="
w-9
h-9
rounded-full
bg-gradient-to-br
from-blue-500
to-purple-500
flex
items-center
justify-center
font-bold
text-white
">

A

</div>



<div className="
hidden
md:block
">

<p className="
text-sm
font-semibold
text-white
">

Admin User

</p>


<p className="
text-xs
text-green-400
">

● Online

</p>


</div>



<ChevronDown
size={16}
className="text-slate-400"
/>


</div>




</div>


</motion.header>


)

}



export default Topbar;