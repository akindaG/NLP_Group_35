import { motion } from "framer-motion";


function ConfidenceMeter({score=94.2}){


return (

<div className="
mt-8
">


<div className="
flex
justify-between
mb-3
">


<p className="
text-slate-400
">

AI Confidence Score

</p>


<p className="
text-green-400
font-bold
">

{score}%


</p>


</div>





<div className="
h-3
bg-slate-800
rounded-full
overflow-hidden
">


<motion.div

initial={{
width:0
}}

animate={{
width:`${score}%`
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




<p className="
mt-3
text-sm
text-green-400
">

Very High Confidence

</p>



</div>

)


}


export default ConfidenceMeter;