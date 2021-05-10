import {useEffect, useState} from 'react'
import Button from './Button'

const Editor = ({name,theme,buttons,code,setCode}) => {

    const [lines,setLines] = useState([1])

    const handleChange = (e) =>{
        
        setCode(e.target.value)

        if(e.target.value === '')
        {
            setLines([1])
            return 
        }

        checkLines(code)

    }

    const checkLines =(code) =>
    {
        const counter = code.split('\n').length 
        let newLines = []

        for(let i =1 ;i<=counter;i++)
            newLines.push(i)

        setLines(newLines)
    }

    useEffect(()=>{
        checkLines(code)
    },[code])

    return(
        <>
            <div className={`h-full border-r border-${theme.borderColor}`}>
                <div className={`editor-top flex flex-row justify-between items-center  bg-${theme.editorBgColor1}  border-b border-${theme.borderColor}`}>
                    <h1 className={`min-h-full text-${theme.text} bg-${theme.editorBgColor2} text-lg font-normal tracking-wide py-4 px-7 border-r  border-${theme.borderColor} `}>
                        {name}
                    </h1>
                    <div className="p-3">
                        {buttons.map((button,index) =>{
                            return <Button key = {index} icon={button.icon} func={button.func}/>
                        })}
                    </div>
                </div>
                <div className={`editor-bottom grid grid-cols-12 text-${theme.text} text-sm font-light`}>
                    <div className={`col-span-1 bg-${theme.editorBgColor2}`}>
                       {
                           lines.map(line =>{
                               return(
                                <div key={line} className={`flex flex-col items-center h-6`}>{line}</div>
                               )
                           })
                       }
                    </div>
                    <textarea 
                        onChange={handleChange}
                        className ={`col-span-11  text-${theme.text} bg-${theme.editorBgColor2} pl-2 leading-6 outline-none resize-none`}
                        value={code}
                    >
                    </textarea>
                </div>
            </div>
        </>
    )
}
 
export default Editor;