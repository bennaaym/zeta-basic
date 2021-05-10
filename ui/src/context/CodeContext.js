import {useState,createContext} from 'react'
import axios from 'axios'

export const CodeContext = createContext()

const CodeContextProvide = ({children}) => {

    const[code,setCode] = useState('PRINT "Hello World";')
    const[output,setOutput] = useState('')


    const runCode = (code) => 
    {
        setCode(code)

        let i = code.length - 1
        for (i;i>0;)
        {
            if(code[i] === ';' || code[i] === '\n')
                i--
            else 
                break;
        }
        const newCode = code.substring(0,i+1)
        axios.post('http://127.0.0.1:5000/api/input',{input:newCode})
        .then(res=>{
            const data = res.data['outputs']
            let out =''
            data.forEach(data =>{
                 out +=data.value+'\n'
            })
            
            setOutput(out)
        })
        .catch(e=>{
            alert("not able to connect to the server, please try again")
        })
    }


    return (
        <CodeContext.Provider value={{
            code,
            setCode,
            output,
            runCode,
            setOutput,
        }}>
            {children}
        </CodeContext.Provider>
    );
}
 
export default CodeContextProvide;