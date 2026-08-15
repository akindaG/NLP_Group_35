import { motion } from "framer-motion";
import {
    Brain,
    Zap,
    Route,
    Search
} from "lucide-react";


function Features(){


const features = [

{
number:"01",
icon:Brain,
tag:"Machine Learning",
title:"NLP Ticket Classification",
description:
"Automatically understand and categorize customer support tickets using advanced Natural Language Processing models."
},

{
number:"02",
icon:Zap,
tag:"Prediction Engine",
title:"Priority Prediction",
description:
"Identify critical customer issues and prioritize tickets using AI confidence scoring and intelligent analysis."
},

{
number:"03",
icon:Route,
tag:"Smart Automation",
title:"Intelligent Routing",
description:
"Automatically recommend the correct support department using semantic understanding of ticket content."
},

{
number:"04",
icon:Search,
tag:"Transparency",
title:"Explainable AI",
description:
"Reveal prediction confidence, important keywords, and insights behind every AI decision."
}

];



return (

<section
className="
relative
pt-40
pb-32
bg-slate-950
text-white
overflow-hidden
"
>


{/* Background Effects */}


<div
className="
absolute
top-0
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
absolute
bottom-0
right-0
w-96
h-96
bg-purple-600/10
blur-[130px]
rounded-full
"
/>






<div
className="
relative
max-w-7xl
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

whileInView={{
opacity:1,
y:0
}}

viewport={{
once:true
}}

transition={{
duration:0.7
}}

className="
text-center
mb-20
"

>


<div
className="
inline-flex
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

AI Powered Intelligence

</div>



<h2
className="
text-4xl
md:text-6xl
font-bold
"
>

Transform Customer Support
<br/>

<span className="text-blue-400">
with Artificial Intelligence
</span>

</h2>



<p
className="
mt-6
text-slate-400
text-lg
max-w-3xl
mx-auto
"
>

SupportIQ combines NLP,
machine learning, and explainable AI
to automate customer support intelligence.

</p>


</motion.div>









{/* Cards */}


<div
className="
grid
md:grid-cols-2
lg:grid-cols-4
gap-7
"
>


{
features.map((feature,index)=>{


const Icon = feature.icon;


return (


<motion.div


key={feature.number}


initial={{
opacity:0,
y:60
}}


whileInView={{
opacity:1,
y:0
}}


viewport={{
once:true
}}


transition={{
duration:0.6,
delay:index*0.15
}}


whileHover={{
y:-12,
scale:1.03
}}

animate={{
y:[0,-5,0]
}}

transition={{
duration:4,
repeat:Infinity,
delay:index*0.5
}}



className="
group
relative
rounded-3xl
p-7
bg-white/5
border
border-white/10
backdrop-blur-xl
overflow-hidden
hover:border-blue-400/40
transition-all
duration-300
"

>





{/* Hover Gradient */}


<div
className="
absolute
inset-0
bg-gradient-to-br
from-blue-500/20
via-transparent
to-purple-500/10
opacity-0
group-hover:opacity-100
transition
"
/>






<div
className="
relative
"
>



<div
className="
flex
justify-between
items-center
mb-7
"
>



<motion.div

whileHover={{
rotate:10
}}

className="
p-4
rounded-2xl
bg-blue-500/10
border
border-blue-400/20
"

>

<Icon
size={36}
className="text-blue-400"
/>


</motion.div>




<span
className="
text-5xl
font-bold
text-white/10
"
>

{feature.number}

</span>


</div>







<span
className="
inline-block
text-xs
px-3
py-1
rounded-full
bg-blue-500/10
text-blue-300
mb-4
"
>

{feature.tag}

</span>







<h3
className="
text-xl
font-semibold
mb-4
"
>

{feature.title}

</h3>







<p
className="
text-slate-400
leading-relaxed
"
>

{feature.description}

</p>





</div>


</motion.div>


)


})


}


</div>










{/* Stats Section */}


<motion.div

initial={{
opacity:0,
y:30
}}

whileInView={{
opacity:1,
y:0
}}

viewport={{
once:true
}}

className="
grid
md:grid-cols-3
gap-10
mt-20
max-w-4xl
mx-auto
text-center
"

>


<div
className="
bg-white/5
border
border-white/10
rounded-2xl
p-8
backdrop-blur-xl
hover:border-blue-400/30
transition
"
>

<h3 className="
text-4xl
font-bold
text-blue-400
">

6+

</h3>

<p className="text-slate-400 mt-2">
AI Models Supported
</p>

</div>




<div
className="
bg-white/5
border
border-white/10
rounded-2xl
p-8
backdrop-blur-xl
hover:border-blue-400/30
transition
"
>

<h3 className="
text-4xl
font-bold
text-blue-400
">

Real-Time

</h3>

<p className="text-slate-400 mt-2">
Ticket Intelligence
</p>

</div>





<div
className="
bg-white/5
border
border-white/10
rounded-2xl
p-8
backdrop-blur-xl
hover:border-blue-400/30
transition
"
>

<h3 className="
text-4xl
font-bold
text-blue-400
">

NLP

</h3>

<p className="text-slate-400 mt-2">
Powered Analytics
</p>

</div>



</motion.div>







{/* Next Section Bridge */}


<motion.div

initial={{
opacity:0
}}

whileInView={{
opacity:1
}}

viewport={{
once:true
}}

className="
text-center
mt-20
"

>


<p className="
text-slate-400
"
>

Built with modern NLP architectures,
machine learning algorithms,
and transformer-based AI models.

</p>


</motion.div>





</div>


</section>


)

}


export default Features;