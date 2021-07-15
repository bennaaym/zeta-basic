import {useState,useEffect,createContext} from 'react'


export const ThemeContext = createContext();


const ThemeContextProvider = ({children}) => {
    


    const [theme,setTheme] = useState({
        isLight : true,
        light:{
            text:'gray-800',
            navBgColor:'',
            editorBgColor1:'gray-50',
            editorBgColor2:'gray-150',
            borderColor:'gray-black'
        },
        dark:{
            text:'gray-100',
            navBgColor:'gray-900',
            editorBgColor1:'gray-900',
            editorBgColor2:'gray-800',
            borderColor:'gray-700'
        }
    },)

    const toggleTheme = () =>{
        setTheme({...theme,isLight:!theme.isLight})
    }

    useEffect(()=>{
        const localTheme = localStorage.getItem('theme')
        if(localTheme)
            setTheme(JSON.parse(localTheme))
    },[])

    useEffect(()=>{
        localStorage.setItem('theme',JSON.stringify(theme))
    },[theme])

    return ( 
       <ThemeContext.Provider value={
          {
            theme,
            toggleTheme
          }
       }>
           {children}
       </ThemeContext.Provider>
     );

}
 
export default ThemeContextProvider;