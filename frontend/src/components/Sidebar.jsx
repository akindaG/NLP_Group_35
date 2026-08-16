import {getHealth} from "../services/api";
import { useEffect, useState } from "react";
import {
    LayoutDashboard,
    Brain,
    BarChart3,
    Settings,
    Activity,
    FileSearch,
    ChevronRight,
    ShieldCheck,
    Cpu,
    Zap
} from "lucide-react";

import { NavLink } from "react-router-dom";


function Sidebar(){
    const [health, setHealth] = useState({
    status: "checking",
    models: "loading"
});

useEffect(() => {

    fetch("http://127.0.0.1:8000/health")
        .then(res => res.json())
        .then(data => {
            setHealth(data);
        })
        .catch(() => {
            setHealth({
                status:"offline",
                models:"unavailable"
            });
        });

}, []);

useEffect(()=>{

getHealth()
.then(data=>setHealth(data))
.catch(()=>{});

},[]);


const menuGroups=[

{
title:"MAIN",
items:[
{
name:"Dashboard",
path:"/dashboard",
icon:LayoutDashboard
},
{
name:"AI Analyzer",
path:"/analyzer",
icon:Brain
}
]
},


{
title:"INTELLIGENCE",
items:[
{
name:"Analytics",
path:"#",
icon:BarChart3
},

{
name:"AI Models",
path:"#",
icon:Cpu
},

{
name:"Predictions",
path:"#",
icon:Activity
}

]
},


{
title:"SYSTEM",
items:[
{
name:"Reports",
path:"#",
icon:FileSearch
},

{
name:"Security",
path:"#",
icon:ShieldCheck
},

{
name:"Settings",
path:"#",
icon:Settings
}

]
}

];



return (

<aside
className="
w-64
min-h-screen
bg-[#050816]
border-r
border-white/10
p-5
flex
flex-col
"
>



{/* BRAND */}

<div
className="
flex
items-center
gap-3
mb-10
"
>


<div
className="
w-11
h-11
rounded-xl
bg-blue-500/20
border
border-blue-500/30
flex
items-center
justify-center
text-blue-400
shadow-lg
shadow-blue-500/20
"
>

<Brain size={24}/>

</div>



<div>

<h1
className="
text-lg
font-bold
text-white
"
>
SupportIQ
</h1>


<p
className="
text-[11px]
text-slate-400
"
>
Enterprise AI Operations
</p>


</div>


</div>





{/* MENU */}


<div
className="
space-y-7
"
>


{
menuGroups.map((group)=>(


<div
key={group.title}
>


<p
className="
text-[10px]
uppercase
tracking-widest
text-slate-500
mb-3
px-2
"
>

{group.title}

</p>




<div
className="
space-y-2
"
>


{
group.items.map((item)=>{


const Icon=item.icon;



return(


<NavLink

key={item.name}

to={item.path}

className={({isActive})=>

`
group
flex
items-center
justify-between
px-3
py-3
rounded-xl
transition-all
duration-300

${
isActive

?

"bg-blue-500/20 text-blue-400 border border-blue-500/30 shadow-lg shadow-blue-500/10"

:

"text-slate-400 hover:text-white hover:bg-white/5"

}

`

}


>


<div
className="
flex
items-center
gap-3
"
>


<Icon
size={18}
className="
group-hover:scale-110
transition
"
/>


<span
className="
text-sm
"
>

{item.name}

</span>


</div>



<ChevronRight
size={14}
className="
opacity-50
"
/>


</NavLink>


)


})

}



</div>


</div>


))

}


</div>






{/* AI ENGINE STATUS */}



<div
className="
mt-auto
mb-4
rounded-2xl
p-4
bg-gradient-to-br
from-blue-500/20
to-purple-500/10
border
border-blue-500/20
"
>


<div
className="
flex
items-center
gap-2
mb-3
"
>

<Zap
size={16}
className="
text-yellow-400
"
/>


<p
className="
text-sm
font-semibold
"
>

AI Engine

</p>


</div>



<div
className="
space-y-2
text-xs
"
>


<p
className="
text-green-400
"
>
● DistilBERT Online
</p>


<p
className="
text-green-400
"
>
● XGBoost Ready
</p>


<p
className="
text-blue-300
"
>
⚡ Latency {health?.latency || "--"}ms
</p>


</div>


</div>







{/* USER */}


<div
className="
bg-white/5
border
border-white/10
rounded-xl
p-3
"
>


<div
className="
flex
items-center
gap-3
"
>


<div
className="
w-10
h-10
rounded-full
bg-gradient-to-br
from-blue-500
to-purple-500
flex
items-center
justify-center
font-bold
"
>

A

</div>



<div>

<p
className="
text-sm
font-semibold
"
>

Admin User

</p>


<p
className="
text-xs
text-green-400
"
>

● Online

</p>


</div>



</div>



</div>



</aside>


)

}


export default Sidebar;