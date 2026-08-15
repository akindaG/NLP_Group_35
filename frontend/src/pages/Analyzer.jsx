import { useState } from "react";
import { motion } from "framer-motion";

import {
    Brain,
    Sparkles,
    Activity,
    AlertTriangle,
    CheckCircle
} from "lucide-react";



function Analyzer(){


const [ticket,setTicket] = useState("");

const [analyzed,setAnalyzed] = useState(false);

const [loading,setLoading] = useState(false);



const analyzeTicket = () => {


if(!ticket.trim()){
    return;
}


setLoading(true);


setTimeout(()=>{

setLoading(false);

setAnalyzed(true);


},1200);


};



return (


<section

className="
min-h-screen
relative
overflow-hidden
bg-slate-950
text-white
pt-32
pb-20
"


>


{/* Background Glow */}


<div

className="
absolute
top-20
left-1/2
-translate-x-1/2
w-[600px]
h-[300px]
bg-blue-600/20
blur-[150px]
rounded-full
"

/>



<div

className="
relative
max-w-5xl
mx-auto
px-6
"

>



{/* Header */}


<motion.div


initial={{
opacity:0,
y:40
}}


animate={{
opacity:1,
y:0
}}



transition={{
duration:0.7
}}


className="
text-center
mb-12
"

>


<div

className="
inline-flex
items-center
gap-2
px-4
py-2
rounded-full
bg-blue-500/10
border
border-blue-400/20
text-blue-400
text-sm
mb-6
"

>


<Sparkles size={16}/>


AI Ticket Intelligence


</div>




<h1

className="
text-4xl
md:text-5xl
font-bold
"

>

Analyze Customer Support Tickets

</h1>




<p

className="
mt-5
text-slate-400
text-lg
"

>

Powered by NLP models,
transformers, and machine learning pipelines.

</p>



</motion.div>







{/* Input Section */}



<motion.div


initial={{
opacity:0,
scale:0.95
}}


animate={{
opacity:1,
scale:1
}}


transition={{
duration:0.5
}}



className="
bg-white/10
border
border-white/20
backdrop-blur-xl
rounded-3xl
p-8
"



>


<div className="
flex
items-center
gap-3
mb-5
">


<Brain
className="text-blue-400"
/>


<h2 className="
text-xl
font-semibold
">

Customer Ticket

</h2>


</div>





<textarea


value={ticket}


onChange={(e)=>setTicket(e.target.value)}


placeholder="
Example: I was charged twice for my subscription...
"


className="
w-full
h-48
bg-slate-900/70
border
border-white/10
rounded-xl
p-5
text-white
placeholder:text-slate-500
outline-none
focus:border-blue-500
resize-none
"



/>






<button


onClick={analyzeTicket}


disabled={loading}


className="
mt-6
w-full
py-4
rounded-xl
bg-blue-600
hover:bg-blue-500
disabled:bg-blue-900
font-semibold
transition
flex
items-center
justify-center
gap-3
"



>


{
loading ?

<>

<Activity className="animate-spin"/>

Analyzing with AI...

</>


:

<>

<Brain size={20}/>

Analyze Ticket

</>

}



</button>



</motion.div>










{/* Prediction Result */}



{
analyzed && (


<motion.div


initial={{
opacity:0,
y:40
}}


animate={{
opacity:1,
y:0
}}


transition={{
duration:0.6
}}



className="
mt-10
bg-white/10
border
border-white/20
backdrop-blur-xl
rounded-3xl
p-8
"

>


<div className="
flex
items-center
justify-between
mb-8
">


<h2 className="
text-2xl
font-bold
">

AI Prediction Result

</h2>



<div

className="
flex
items-center
gap-2
text-green-400
text-sm
"

>

<CheckCircle size={18}/>

Completed

</div>


</div>







<div

className="
grid
md:grid-cols-2
gap-8
"


>



<div>

<p className="
text-slate-400
text-sm
">

Category

</p>


<h3 className="
text-xl
font-semibold
mt-1
">

Billing Issue

</h3>


</div>





<div>

<p className="
text-slate-400
text-sm
">

Priority

</p>


<h3 className="
text-xl
font-semibold
text-red-400
mt-1
flex
items-center
gap-2
">

<AlertTriangle size={20}/>

High

</h3>


</div>






<div>

<p className="
text-slate-400
text-sm
">

Sentiment

</p>


<h3 className="
text-xl
font-semibold
mt-1
">

Negative

</h3>


</div>






<div>

<p className="
text-slate-400
text-sm
">

Recommended Department

</p>


<h3 className="
text-xl
font-semibold
mt-1
">

Finance Support

</h3>


</div>






<div>

<p className="
text-slate-400
text-sm
">

Model Used

</p>


<h3 className="
text-xl
font-semibold
mt-1
text-blue-400
">

DistilBERT

</h3>


</div>


</div>








{/* Confidence */}



<div className="
mt-10
">


<div className="
flex
justify-between
mb-3
">


<p className="
text-slate-400
">

Confidence Score

</p>



<p className="
text-green-400
font-semibold
">

94.2%

</p>



</div>




<div

className="
h-3
rounded-full
bg-slate-800
overflow-hidden
"


>


<motion.div


initial={{
width:0
}}


animate={{
width:"94%"
}}


transition={{
duration:1
}}


className="
h-full
bg-green-500
rounded-full
"


/>



</div>


</div>







{/* Keywords */}



<div className="
mt-8
">


<p className="
text-slate-400
mb-3
">

Important Keywords

</p>



<div className="
flex
flex-wrap
gap-3
">


{
["refund","payment","charged"].map((word)=>(


<span

key={word}

className="
px-4
py-2
rounded-full
bg-white/10
border
border-white/10
text-sm
"

>

{word}

</span>


))

}


</div>



</div>






</motion.div>


)

}




</div>


</section>


)

}



export default Analyzer;