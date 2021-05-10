import Head from "./Head"
import ListItem from "./ListItem"
import {documentation,datatypes,codeExamples} from "../../documentation"

const Guide = ({theme}) => {

    return ( 

                <div className={`guide grid grid-cols-12 bg-${theme.editorBgColor1} `}>
                <div className ='col-start-3 col-end-10 pt-12'>
                    <section className="about mb-12">
                        <Head 
                            theme={theme}
                            title = {`About ${String.fromCharCode(950)} basic`}
                            textSize={'xl'}
                            fontWeight = {'bold'}
                            margin={'8'}/>

                        <div className={`text-${theme.text} leading-7 pl-7 `}>
                            <p>
                                <strong className="text-gray-700 ">&#950; basic </strong>
                                basic is a small interpreted programming language based on python. Its syntax is mainly inspired by the BASIC language.
                            </p>
                        </div>                        
                    </section>

                    <section className="documentation mb-12">
                        <Head 
                            theme={theme}
                            title = {`${String.fromCharCode(950)} basic documentation`}
                            textSize={'xl'}
                            fontWeight = {'bold'}
                            margin={'8'}/>
                        <div className={`text-${theme.text} leading-7 pl-7 `}>
                            <ul className="list-disc">
                                <ListItem
                                        theme={theme}
                                        name = {'datatypes'}
                                        text={[[String.fromCharCode(950)+' basic has '+datatypes.length+' data types']]}
                                        textSize={'lg'}
                                        fontWeight={'medium'}
                                        margin={'4'}
                                        padding={'7'}
                                        items={datatypes}
                                                
                                    />
                                {
                                    documentation.map((doc,index)=>
                                    {
                                        return (
                                            <ListItem
                                                key={index} 
                                                theme={theme}
                                                name = {doc.name}
                                                text={doc.description}
                                                textSize={'lg'}
                                                fontWeight={'medium'}
                                                margin={'4'}
                                                exemples={doc.exemples}
                                                play={true}
                                            />)
                                    })
                                }
                            </ul>
                        </div> 
                    </section>

                    <section className="about mb-12">
                        <Head 
                            theme={theme}
                            title = {`${String.fromCharCode(950)} basic code examples`}
                            textSize={'xl'}
                            fontWeight = {'bold'}
                            margin={'8'}/>

                        <div className={`text-${theme.text} leading-7 pl-7 `}>
                        <ul className="list-disc">
                                {
                                    codeExamples.map((code,index)=>
                                    {
                                        return (
                                            <ListItem
                                                key={index} 
                                                theme={theme}
                                                name = {code.name}
                                                text={code.description}
                                                textSize={'lg'}
                                                fontWeight={'medium'}
                                                margin={'4'}
                                                exemples={code.exemples}
                                                play={true}
                                            />)
                                    })
                                }
                            </ul>
                        </div>                        
                    </section>
                </div>
            </div>
            )
   
}
 
export default Guide;