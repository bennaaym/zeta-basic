import Button from "./Button"
import {faPlayCircle} from '@fortawesome/free-solid-svg-icons'
import {CodeContext} from "../../context/CodeContext"
import {useHistory} from 'react-router-dom'
import {useContext} from 'react'

const SyntaxExemple = ({play,syntax}) => {
    const {runCode} = useContext(CodeContext)
    const history = useHistory()
    const copyCode = (runCode) =>{
        let code = ''
        syntax.forEach((exper)=>{
            code += exper+'\n'
        })
        runCode(code)

        history.push('/')
    }

    return ( 

            <div className={`bg-gray-700  rounded p-5 mt-4 leading-6`}>
                {
 

                    syntax.map((s,index) =>{
                            return  <p key={index} className="text-gray-200 text-sm mb-2">{s} </p>
                    })
                }
                {
                    
                    (play  && !(syntax[0].includes('Syntax')) && <div className="flex w-full justify-end ">
                        <Button icon={faPlayCircle} func={() => copyCode(runCode)} />
                    </div>)
                }
            </div>

    );
}
 
export default SyntaxExemple;