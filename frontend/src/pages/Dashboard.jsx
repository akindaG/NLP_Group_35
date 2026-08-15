import { motion } from "framer-motion";

import {
    Ticket,
    AlertTriangle,
    Brain,
    TrendingUp,
    Activity,
    Cpu,
    CheckCircle,
    BarChart3,
    ShieldCheck,
    Sparkles,
    Clock,
    ArrowUpRight,
    Zap,
    Target,
    Network
} from "lucide-react";


import {
    PieChart,
    Pie,
    Cell,
    ResponsiveContainer,
    LineChart,
    Line,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid
} from "recharts";



function Dashboard(){


const stats=[

{
icon:Ticket,
title:"Total Tickets",
value:"12,450",
change:"+18.5%",
description:"Processed through AI pipeline"
},

{
icon:AlertTriangle,
title:"Critical Tickets",
value:"1,240",
change:"-8.2%",
description:"Require immediate attention"
},

{
icon:Brain,
title:"AI Accuracy",
value:"94.2%",
change:"+2.4%",
description:"Prediction confidence"
},

{
icon:TrendingUp,
title:"Resolution Rate",
value:"87%",
change:"+12%",
description:"Support efficiency"
}

];




const categories=[

{
name:"Billing Issues",
value:75
},

{
name:"Technical Problems",
value:60
},

{
name:"Account Support",
value:45
},

{
name:"Payment Requests",
value:35
}

];




const models=[

{
name:"DistilBERT Classifier",
type:"Ticket Classification",
accuracy:"94.2%",
latency:"120ms"
},

{
name:"XGBoost Priority Engine",
type:"Priority Prediction",
accuracy:"91.8%",
latency:"85ms"
},

{
name:"Sentiment Analyzer",
type:"Emotion Detection",
accuracy:"92.6%",
latency:"95ms"
}

];




const activities=[

{
time:"09:42",
text:"DistilBERT classified ticket #12450",
status:"Completed"
},

{
time:"09:43",
text:"XGBoost detected high priority issue",
status:"Warning"
},

{
time:"09:44",
text:"Sentiment analysis completed",
status:"Completed"
},

{
time:"09:45",
text:"Ticket routed to Finance Support",
status:"Completed"
}

];




const tickets=[

{
id:"#12401",
category:"Billing Issue",
priority:"High",
sentiment:"Negative",
confidence:96
},

{
id:"#12402",
category:"Technical",
priority:"Medium",
sentiment:"Neutral",
confidence:91
},

{
id:"#12403",
category:"Account",
priority:"Low",
sentiment:"Positive",
confidence:95
},

{
id:"#12404",
category:"Payment",
priority:"High",
sentiment:"Negative",
confidence:93
}

];




const sentimentData=[

{
name:"Positive",
value:45
},

{
name:"Neutral",
value:35
},

{
name:"Negative",
value:20
}

];



const ticketTrend=[

{
time:"9AM",
tickets:120
},

{
time:"10AM",
tickets:180
},

{
time:"11AM",
tickets:260
},

{
time:"12PM",
tickets:320
},

{
time:"1PM",
tickets:410
}

];



const routingData=[

{
department:"Finance",
tickets:420
},

{
department:"Technical",
tickets:350
},

{
department:"Account",
tickets:220
},

{
department:"Security",
tickets:90
}

];



const COLORS=[
"#22c55e",
"#3b82f6",
"#ef4444"
];



return (

<section

className="
min-h-screen
bg-slate-950
text-white
relative
overflow-hidden
py-32
"

>


<div

className="
absolute
top-0
left-1/2
-translate-x-1/2
w-[900px]
h-[400px]
bg-blue-600/20
blur-[160px]
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


{/* HEADER */}


<motion.div

initial={{
opacity:0,
y:40
}}

animate={{
opacity:1,
y:0
}}

className="mb-14"

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
"

>

<Sparkles size={16}/>

AI Support Intelligence

</div>



<div className="
flex
justify-between
items-center
mt-6
">


<div>


<h1

className="
text-5xl
font-bold
"

>

Enterprise AI Dashboard

</h1>


<p

className="
text-slate-400
mt-4
text-lg
"

>

Real-time NLP monitoring platform for
ticket classification, sentiment analysis,
priority prediction and routing.

</p>


</div>



<div

className="
hidden
md:flex
items-center
gap-3
bg-green-500/10
border
border-green-400/20
px-5
py-3
rounded-2xl
text-green-400
"

>


<div

className="
w-3
h-3
rounded-full
bg-green-400
animate-pulse
"

/>

AI System Online


</div>


</div>


</motion.div>

{/* KPI CARDS */}


<div

className="
grid
md:grid-cols-2
lg:grid-cols-4
gap-6
"

>


{

stats.map((item,index)=>{


const Icon=item.icon;


return(

<motion.div


key={item.title}


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


transition={{
delay:index*0.1
}}


whileHover={{
y:-8
}}


className="
relative
overflow-hidden
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-6
"


>


<div

className="
absolute
inset-0
bg-gradient-to-br
from-blue-500/20
to-transparent
opacity-0
hover:opacity-100
transition
"

/>



<div className="relative">


<div

className="
flex
justify-between
items-center
"

>


<div

className="
p-3
rounded-2xl
bg-blue-500/10
"

>

<Icon

size={28}

className="text-blue-400"

/>


</div>



<div

className="
flex
items-center
gap-1
text-green-400
text-sm
"

>

{item.change}

<ArrowUpRight size={14}/>

</div>


</div>




<h2

className="
text-4xl
font-bold
mt-6
"

>

{item.value}

</h2>



<h3

className="
font-semibold
mt-2
"

>

{item.title}

</h3>


<p

className="
text-slate-400
text-sm
mt-2
"

>

{item.description}

</p>


</div>


</motion.div>


)


})


}


</div>









{/* ANALYTICS SECTION */}


<div

className="
grid
lg:grid-cols-3
gap-8
mt-10
"

>



{/* CATEGORY ANALYSIS */}



<div

className="
lg:col-span-2
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-8
"

>

<BarChart3

className="text-blue-400"

/>


<h2

className="
text-xl
font-semibold
"

>

Ticket Intelligence Overview

</h2>


</div>



{

categories.map(item=>(


<div

key={item.name}

className="
mb-6
"

>


<div

className="
flex
justify-between
mb-2
text-sm
"

>


<span>

{item.name}

</span>


<span

className="text-blue-400"

>

{item.value}%

</span>


</div>



<div

className="
h-3
bg-slate-800
rounded-full
overflow-hidden
"

>


<motion.div


initial={{
width:0
}}


whileInView={{
width:`${item.value}%`
}}


transition={{
duration:1
}}


className="
h-3
bg-gradient-to-r
from-blue-500
to-cyan-400
rounded-full
"

/>


</div>



</div>


))


}


</div>







{/* SYSTEM HEALTH */}



<div

className="
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-8
"

>


<ShieldCheck

className="text-green-400"

/>


<h2

className="
text-xl
font-semibold
"

>

System Health

</h2>


</div>



<div className="space-y-5">


{

[
"API Gateway Online",
"NLP Pipeline Active",
"AI Models Loaded",
"Database Connected"

].map(item=>(


<div

key={item}

className="
flex
items-center
gap-3
"

>


<div

className="
p-2
rounded-xl
bg-green-500/10
"

>


<CheckCircle

size={18}

className="
text-green-400
"

/>


</div>



<span>

{item}

</span>



</div>


))


}


</div>


</div>



</div>









{/* ADVANCED ANALYTICS CHARTS */}



<div

className="
grid
lg:grid-cols-3
gap-8
mt-10
"

>





{/* SENTIMENT PIE */}



<div

className="
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-6
"

>

<Target

className="text-blue-400"

/>


<h2 className="font-semibold">

Sentiment Intelligence

</h2>


</div>




<ResponsiveContainer

width="100%"

height={250}

>


<PieChart>


<Pie

data={sentimentData}

dataKey="value"

outerRadius={90}

innerRadius={50}

paddingAngle={5}

>


{

sentimentData.map(
(entry,index)=>(

<Cell

key={entry.name}

fill={COLORS[index]}

/>

)

)

}


</Pie>


<Tooltip/>


</PieChart>


</ResponsiveContainer>



<div className="space-y-3">


{

sentimentData.map((item,index)=>(


<div

key={item.name}

className="
flex
justify-between
text-sm
"

>

<span>

{item.name}

</span>


<span

className="text-blue-400"

>

{item.value}%

</span>


</div>


))


}


</div>



</div>








{/* TICKET TREND */}



<div

className="
lg:col-span-2
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-6
"

>


<Activity

className="text-blue-400"

/>


<h2 className="font-semibold">

Live Ticket Processing Trend

</h2>


</div>




<ResponsiveContainer

width="100%"

height={280}

>


<LineChart

data={ticketTrend}

>


<CartesianGrid

strokeDasharray="3 3"

/>


<XAxis

dataKey="time"

/>


<YAxis/>


<Tooltip/>


<Line

type="monotone"

dataKey="tickets"

strokeWidth={3}

/>


</LineChart>


</ResponsiveContainer>


</div>



</div>

{/* DEPARTMENT ROUTING ANALYTICS */}


<div

className="
mt-10
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-8
"

>


<Network

className="text-blue-400"

/>


<h2

className="
text-xl
font-semibold
"

>

Department Routing Intelligence

</h2>


</div>




<ResponsiveContainer

width="100%"

height={300}

>


<BarChart

data={routingData}

>


<CartesianGrid

strokeDasharray="3 3"

/>


<XAxis

dataKey="department"

/>


<YAxis/>


<Tooltip/>


<Bar

dataKey="tickets"

/>


</BarChart>


</ResponsiveContainer>



</div>









{/* LIVE PROCESSING ACTIVITY */}



<div

className="
mt-10
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-8
"

>


<Clock

className="text-blue-400"

/>


<h2

className="
text-xl
font-semibold
"

>

Live AI Processing Activity

</h2>


</div>





<div

className="
grid
md:grid-cols-4
gap-5
"

>


{

activities.map(item=>(


<motion.div


whileHover={{
y:-5
}}


key={item.time}


className="
rounded-2xl
bg-slate-900/60
border
border-white/10
p-5
"

>


<div

className="
flex
justify-between
text-sm
mb-4
"

>


<span

className="text-blue-400"

>

{item.time}

</span>



<div

className="
w-2
h-2
rounded-full
bg-green-400
"

/>


</div>



<p

className="
text-sm
text-slate-300
"

>

{item.text}

</p>



<p

className="
text-green-400
text-xs
mt-4
"

>

{item.status}

</p>



</motion.div>


))


}


</div>


</div>









{/* MODEL PERFORMANCE */}



<div

className="
mt-10
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-8
"

>


<Cpu

className="text-blue-400"

/>


<h2

className="
text-xl
font-semibold
"

>

AI Model Performance

</h2>


</div>





<div

className="
grid
md:grid-cols-3
gap-6
"

>


{

models.map(model=>(


<motion.div


whileHover={{
scale:1.03
}}


key={model.name}


className="
rounded-2xl
bg-slate-900/70
border
border-white/10
p-6
"

>


<div

className="
flex
items-center
gap-2
text-blue-400
text-sm
"

>


<Zap size={15}/>


{model.type}


</div>



<h3

className="
font-semibold
mt-5
"

>

{model.name}

</h3>



<div

className="
flex
items-end
justify-between
mt-6
"

>


<p

className="
text-4xl
font-bold
text-blue-400
"

>

{model.accuracy}

</p>



<span

className="
text-xs
text-slate-400
"

>

{model.latency}

</span>


</div>



<div

className="
h-2
bg-slate-800
rounded-full
mt-5
"

>


<div

className="
h-2
rounded-full
bg-gradient-to-r
from-blue-500
to-cyan-400
"

style={{
width:model.accuracy
}}

/>


</div>



<p

className="
text-green-400
text-sm
mt-4
"

>

● Production Ready

</p>


</motion.div>


))


}


</div>


</div>









{/* AI EXPLAINABILITY */}



<div

className="
mt-10
rounded-3xl
bg-gradient-to-br
from-blue-500/10
to-purple-500/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<div

className="
flex
items-center
gap-3
mb-8
"

>


<Brain

className="text-purple-400"

/>


<h2

className="
text-xl
font-semibold
"

>

AI Explainability Engine

</h2>


</div>




<div

className="
grid
md:grid-cols-4
gap-6
"

>


<div>

<p className="text-slate-400 text-sm">

Input Ticket

</p>


<p className="mt-2">

"I was charged twice for my subscription"

</p>


</div>



<div>

<p className="text-slate-400 text-sm">

Prediction

</p>


<p className="mt-2 text-blue-400 font-semibold">

Billing Issue

</p>


</div>




<div>

<p className="text-slate-400 text-sm">

Confidence

</p>


<p className="mt-2 text-green-400 font-semibold">

94.2%

</p>


</div>




<div>

<p className="text-slate-400 text-sm">

Routing

</p>


<p className="mt-2">

Finance Support

</p>


</div>



</div>





<div

className="
flex
gap-3
mt-8
flex-wrap
"

>


{

[
"refund",
"charged",
"subscription",
"payment"

].map(word=>(


<span

key={word}

className="
px-4
py-2
rounded-full
bg-purple-500/10
border
border-purple-400/20
text-purple-300
text-sm
"

>

{word}

</span>


))


}


</div>



</div>









{/* RECENT PREDICTIONS TABLE */}



<div

className="
mt-10
rounded-3xl
bg-white/10
border
border-white/20
backdrop-blur-xl
p-8
"

>


<h2

className="
text-xl
font-semibold
mb-8
"

>

Recent AI Predictions

</h2>





<div

className="
overflow-x-auto
"

>


<table

className="
w-full
"

>


<thead>


<tr

className="
text-slate-400
border-b
border-white/10
"

>


<th className="text-left pb-4">
Ticket
</th>


<th>
Category
</th>


<th>
Priority
</th>


<th>
Sentiment
</th>


<th>
Confidence
</th>


</tr>


</thead>




<tbody>


{

tickets.map(ticket=>(


<tr

key={ticket.id}

className="
border-b
border-white/10
"

>


<td className="py-5">

{ticket.id}

</td>



<td>

{ticket.category}

</td>



<td>

<span

className="
px-3
py-1
rounded-full
bg-red-500/10
text-red-400
text-sm
"

>

{ticket.priority}

</span>


</td>



<td>

{ticket.sentiment}

</td>



<td>


<div className="flex items-center gap-3">


<div

className="
w-24
h-2
bg-slate-800
rounded-full
"

>


<div

className="
h-2
bg-blue-500
rounded-full
"

style={{
width:`${ticket.confidence}%`
}}

/>


</div>


<span className="text-blue-400">

{ticket.confidence}%

</span>


</div>


</td>



</tr>


))


}


</tbody>


</table>


</div>


</div>






</div>


</section>


)

}



export default Dashboard;