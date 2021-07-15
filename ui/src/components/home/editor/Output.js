import Button from './Button'
const Output = ({name ,theme, buttons,output}) => {

    return(
        <>
            <div className="h-full">
                <div className={`editor-top flex flex-row justify-between items-center  bg-${theme.editorBgColor1}  border-b border-${theme.borderColor}`}>
                    <h1 className={`min-h-full text-${theme.text} bg-${theme.editorBgColor1} text-md py-5 px-7 `}>
                        {name}
                    </h1>
                    <div className="p-3">
                        {buttons.map((button,index) =>{
                            return <Button key = {index} icon={button.icon} func={button.func}/>
                        })}
                    </div>
                </div>
                <div className={`editor-bottom grid grid-cols-12 text-${theme.text} text-sm font-light`}>
                    <textarea 
                        disabled
                        className ={`col-span-12  bg-${theme.editorBgColor2} pl-2 leading-6 outline-none resize-none`}
                        value={output}
                        spellCheck='false'
                    >
                    </textarea>
                </div>
            </div>
        </>
    )
}
 
export default Output;