import SyntaxExemple from "./SyntaxExemple";
import Head from "./Head"

const ListItem = ({theme,name,text,textSize,fontWeight,margin,padding,exemples,items,play}) => {
    return (
        <>
            <li className="mt-8 ">
                <Head 
                    theme={theme}
                    title = {name}
                    textSize={textSize}
                    fontWeight = {fontWeight}
                    margin= {margin}/>
                {
                    text.map((t,index)=>{
                        
                        return <p key={index} className="text-md font-normal py-1">{t +' .'}</p>
                    })
                }
              
                {exemples &&
                    exemples.map((exemple,index)=>{
                        return (
                            <SyntaxExemple key ={index}
                                syntax ={exemple}
                                play={play}
                            />)
                    })
                }

                {
                  items && (
                      <ul className = {`list-disc pl-${padding}`}>
                        {
                             items.map((item,index)=>{
                                return <li key={index}>{item}</li>
                            })
                        }
                      </ul>
                  )   
                 
                }
            </li>
        </>
    );
}
 
export default ListItem;