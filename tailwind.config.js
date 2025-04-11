/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**.html"
    ],
    theme: {
        extend: {
            colors: {
                'primary': {
                    DEFAULT: '#FCC6C6',
                    50: '#FDD9D9',
                    100: '#FCC6C6',
                    200: '#FBAEAE',
                    300: '#F99696',
                    400: '#F87D7D',
                    500: '#F76565',
                    600: '#F64D4D',
                    700: '#F43535',
                    800: '#F31C1C',
                    900: '#EA0C0C',
                    950: '#DE0C0C'
                },
                'secondary': {
                    DEFAULT: '#68867A',
                    50: '#E4EAE8',
                    100: '#D9E1DE',
                    200: '#C2CFCA',
                    300: '#ABBEB6',
                    400: '#94ACA2',
                    500: '#7D9A8E',
                    600: '#68867A',
                    700: '#566F65',
                    800: '#445850',
                    900: '#33413B',
                    950: '#2A3631'
                },
                'accent': {
                    DEFAULT: '#FF6B69',
                    50: '#FFD5D4',
                    100: '#FFC6C5',
                    200: '#FFA7A6',
                    300: '#FF8988',
                    400: '#FF6B69',
                    500: '#FF4D4A',
                    600: '#FF2F2C',
                    700: '#FF100D',
                    800: '#EE0300',
                    900: '#CF0300',
                    950: '#C00300'
                },
            }
        },
    },
    plugins: [],
}

