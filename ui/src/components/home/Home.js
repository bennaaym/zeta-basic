import {useContext} from 'react'
import Editor from "./editor/Editor"
import {ThemeContext} from "../../context/ThemeContext"
import {faEraser, faMoon,faPlay,faSun} from '@fortawesome/free-solid-svg-icons'
import Output from "./editor/Output"
import {CodeContext} from "../../context/CodeContext"

const Home = () => {
    const {theme,toggleTheme} = useContext(ThemeContext)
    const activeTheme = theme.isLight ? theme.light : theme.dark
    const {code,setCode,runCode,output,setOutput} = useContext(CodeContext)

    return (           
        <div className="home grid grid-cols-2">
            <div className="">
                {<Editor
                            name = {'main'}
                            theme = {activeTheme} 
                            buttons = {[
                                {icon:theme.isLight? faMoon : faSun,func:toggleTheme},
                                {icon:faPlay,func:() => runCode(code)}
                            ]}
                            code = {code}
                            setCode= {setCode}
                />}
            </div>
            <div className="">
                <Output 
                    name='output' 
                    theme = {activeTheme}
                    buttons={[
                    {icon:faEraser,func:()=>setOutput('')}]}
                    output={output}

                />
                
            </div>
        </div>

    );
   
}
 
export default Home