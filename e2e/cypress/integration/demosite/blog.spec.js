/// <reference types="cypress" />

context('Actions', () => {
  beforeEach(() => {
    cy.visit('/blog')
  })

  it('check if modal is visible', () => {
    cy.get('#newsletter-container').should('be.visible')
    cy.get('input[name=name]').should('be.visible')
    cy.get('input[name=email]').should('be.visible')
    cy.get('input[name=permission]').should('be.visible')
    cy.get('button[type=submit]').should('be.visible')
    cy.get('button[type=button].close-modal').should('be.visible')
    cy.get('.close').should('be.visible')
  })

})
