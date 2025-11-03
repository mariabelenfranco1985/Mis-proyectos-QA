describe('Prueba de cierre de sesión en Parabank', () => {

  it('Debe cerrar la sesión correctamente y volver a la página de inicio', () => {
    cy.visit('https://parabank.parasoft.com/')

    // Paso 1: iniciar sesión
    cy.get('input[name="username"]').type('john')
    cy.get('input[name="password"]').type('demo')
    cy.get('input[value="Log In"]').click()

    // Paso 2: verificar que el login fue exitoso
    cy.get('#leftPanel').should('contain.text', 'Accounts Overview')

    // Paso 3: hacer clic en "Log Out"
    cy.contains('Log Out').click()

    // Paso 4: verificar que se redirige a la página inicial
    cy.url().should('include', 'index.htm')
    cy.get('#loginPanel').should('be.visible')
    cy.get('#loginPanel').should('contain.text', 'Customer Login')

    // Mensaje de consola para confirmar
    console.log('✅ Logout realizado correctamente. El usuario volvió a la página inicial.')
  })
})
