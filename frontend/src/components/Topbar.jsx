import { 
    Search,
    Bell,
    Zap,
    Activity,
    Ticket,
    ChevronDown,
    Command
} from "lucide-react";

import { motion } from "framer-motion";



function Topbar(){


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


{/* LEFT BRAND AREA */}


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
hover:border-blue-400/30
transition
"


>


<Search

size={18}

className="
text-slate-400
"

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









{/* RIGHT STATUS AREA */}



<div className="
flex
items-center
gap-3
">





{/* TICKET COUNTER */}



<div

className="
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
"


>


<Ticket

size={18}

className="
text-blue-400
"

/>



<div>


<p className="
text-xs
font-semibold
text-blue-400
">

12,450

</p>


<p className="
text-[10px]
text-slate-400
">

Tickets Processed

</p>


</div>


</div>









{/* API STATUS */}



<div

className="
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
"


>


<div className="
relative
">


<span

className="
absolute
w-3
h-3
rounded-full
bg-green-400
animate-ping
"

/>


<span

className="
relative
block
w-3
h-3
rounded-full
bg-green-400
"

/>


</div>




<div>


<p className="
text-xs
font-semibold
text-green-400
">

API Healthy

</p>


<p className="
text-[10px]
text-slate-400
">

99.9% uptime

</p>


</div>


</div>









{/* AI LATENCY */}



<div

className="
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
"


>


<Zap

size={17}

className="
text-purple-400
"

/>



<div>


<p className="
text-xs
font-semibold
text-purple-400
">

85ms

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



<button

className="
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
hover:bg-white/10
transition
"


>


<Bell

size={19}

className="
text-slate-300
"

/>


<span

className="
absolute
top-2
right-2
w-2
h-2
rounded-full
bg-blue-400
"

/>


</button>









{/* USER PROFILE */}



<div

className="
flex
items-center
gap-3
px-3
py-2
rounded-xl
hover:bg-white/5
transition
cursor-pointer
"


>


<div

className="
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
"

>

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

className="
text-slate-400
"

/>



</div>







</div>



</motion.header>


)


}



export default Topbar;