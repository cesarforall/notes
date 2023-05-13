# NextJs

    npx create-next-app name --use-npm
    npx create-next-app .


Next.js es un marco de desarrollo web de React que permite crear aplicaciones web de alto rendimiento y fácil renderizado tanto en el lado del servidor como en el cliente. A continuación, se muestra un resumen de cómo funciona Next.js:

Renderizado híbrido: Next.js permite el renderizado tanto en el lado del servidor (SSR) como en el cliente (CSR). Esto significa que se puede generar el HTML en el servidor y enviarlo al navegador, lo que mejora el tiempo de carga inicial y la capacidad de SEO. Además, una vez cargada la página, Next.js puede alternar al renderizado en el lado del cliente para ofrecer una experiencia de usuario interactiva.

    // pages/index.js
    import React from 'react';

    function HomePage({ data }) {
    return (
        <div>
        <h1>Welcome to Next.js!</h1>
        <p>{data}</p>
        </div>
    );
    }

    export async function getServerSideProps() {
    // Realizar una llamada a la API o consultar la base de datos
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();

    return {
        props: {
        data,
        },
    };
    }

    export default HomePage;


Enrutamiento dinámico: Next.js tiene un sistema de enrutamiento integrado que permite manejar rutas de manera sencilla. Además de las rutas estáticas, también se pueden definir rutas dinámicas con parámetros variables. Esto facilita la creación de aplicaciones con múltiples páginas y contenido personalizado.

    // pages/posts/[id].js
    import React from 'react';
    import { useRouter } from 'next/router';

    function PostPage() {
    const router = useRouter();
    const { id } = router.query;

    return (
        <div>
        <h1>Post {id}</h1>
        {/* Contenido del post */}
        </div>
    );
    }

    export default PostPage;


Pre-renderizado estático: Next.js permite generar páginas estáticas en tiempo de compilación, lo que significa que se pueden generar versiones HTML estáticas de las páginas y distribuirlas en un servidor de archivos estáticos o un CDN. Esto mejora el rendimiento al servir contenido estático sin necesidad de consultar la base de datos o generar el HTML en cada solicitud.

    // pages/blog.js
    import React from 'react';

    function BlogPage({ posts }) {
    return (
        <div>
        <h1>Blog</h1>
        <ul>
            {posts.map((post) => (
            <li key={post.id}>{post.title}</li>
            ))}
        </ul>
        </div>
    );
    }

    export async function getStaticProps() {
    // Obtener los datos de los posts desde una fuente externa
    const res = await fetch('https://api.example.com/posts');
    const posts = await res.json();

    return {
        props: {
        posts,
        },
    };
    }

    export default BlogPage;

API Routes: Next.js proporciona una forma sencilla de crear API RESTful mediante las API Routes. Estas rutas permiten crear endpoints personalizados y manejar solicitudes HTTP, lo que facilita la creación de servicios web y la interacción con bases de datos u otros sistemas.

    // pages/api/users.js
    export default function handler(req, res) {
    const users = [{ id: 1, name: 'John' }, { id: 2, name: 'Jane' }];

    res.status(200).json(users);
    }


Bundling optimizado: Next.js utiliza webpack por debajo para el empaquetado y optimización de los activos de la aplicación. Aplica técnicas como el código dividido (code splitting) para reducir el tamaño de los paquetes y mejorar el tiempo de carga de la página.

Hot Module Replacement (HMR): Next.js aprovecha la funcionalidad de HMR para actualizar automáticamente los módulos modificados en tiempo real, sin necesidad de recargar la página completa. Esto agiliza el proceso de desarrollo y permite ver los cambios instantáneamente.

En resumen, Next.js combina las ventajas del renderizado en el lado del servidor y del cliente, proporcionando un enrutamiento flexible, pre-renderizado estático, manejo de API y optimización del rendimiento. Esto lo convierte en un marco de desarrollo poderoso para la creación de aplicaciones web modernas y eficientes.